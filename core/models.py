from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    """自定义用户模型"""
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="手机号码")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="头像")
    bio = models.TextField(blank=True, null=True, verbose_name="个人简介")
    
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.username
