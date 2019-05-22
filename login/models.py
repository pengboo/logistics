from django.db import models

# Create your models here.
class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=20, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=256, verbose_name='密码')
    phone = models.CharField(max_length=11, unique=True, verbose_name='手机号码')
    sex = models.CharField(max_length=32, choices=gender, default="男", verbose_name='性别')
    department = models.CharField(max_length=20, verbose_name='部门')
    creat_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-creat_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"