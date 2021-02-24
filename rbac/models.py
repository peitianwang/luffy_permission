from django.db import models

# Create your models here.
class Menu(models.Model):
    title=models.CharField(verbose_name='一级菜单标题',max_length=32)
    icon=models.CharField(verbose_name='图标',null=True,blank=True,max_length=32)


class Permission(models.Model):
    '''
    权限表
    '''
    title=models.CharField(verbose_name='标题',max_length=32)
    url=models.CharField(verbose_name='含正则的URL',max_length=128)
    menu=models.ForeignKey(verbose_name='所属菜单',to=Menu,null=True,blank=True,on_delete=models.CASCADE,help_text='null表示不是菜单,非null表示是二级菜单')
    # icon=models.CharField(verbose_name='图标',null=True,blank=True,max_length=32)

    def __str__(self):
        return self.title

class Role(models.Model):
    title=models.CharField(verbose_name='角色的名称',max_length=32)
    permissions=models.ManyToManyField(verbose_name='拥有的全部权限',to=Permission,blank=True)

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    name=models.CharField(verbose_name='用户名',max_length=32)
    password=models.CharField(verbose_name='密码',max_length=64)
    email=models.EmailField(verbose_name='邮箱')
    roles=models.ManyToManyField(verbose_name='拥有的所有角色',to=Role,blank=True)

    def __str__(self):
        return self.name




