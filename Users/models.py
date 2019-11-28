from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
GENDER_CHOICES = (
    ("male", "男"),
    ("female", "女")
)


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=20, verbose_name="昵称", default="")
    birthday = models.DateTimeField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, verbose_name="性别", max_length=6)
    address = models.CharField(max_length=50, verbose_name="地址", default="")
    mobile = models.CharField(max_length=11, verbose_name="手机号")
    header_img = models.ImageField(upload_to="media/image/head_image/%Y/%m", verbose_name="头像",
                                   default="default.png")

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name
        # tb_table=""         # 可以自定义用户表名

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username