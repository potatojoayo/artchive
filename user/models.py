from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import pathlib

# Create your models here.
#
# 유저 매니저 클래스
# 유저와 수퍼유저 생성 시 호출
# create_user()와 create_superuser()
#


class UserManager(BaseUserManager):

    use_in_migrations = True

    # 일반 유저 생성
    def create_user(self, email, name, nickname, password=None):

        if not email:
            raise ValueError('이메일은 필수 입력사항입니다.')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            nickname=nickname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 수퍼 유저 생성
    def create_superuser(self, email, name, password, nickname,):

        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password,
            nickname=nickname
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

#
# 새로운 유저 클래스
#


class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()

    # 필수 필드들 (기본 유저 필드)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    # auto_now_add = 처음 만든 날짜가 저장 됨(고정)
    # cf) auto_now = save()할 때 마다 업데이트됨
    date_joined = models.DateTimeField(auto_now_add=True)

    # 커스텀 필드
    name = models.CharField(max_length=20, null=False)
    nickname = models.CharField(max_length=20, null=False, unique=True)
    email = models.EmailField(max_length=255, null=False, unique=True)
    avatar = models.CharField(max_length=255, null=False,
                              default='https://artchivepotatojoayo.s3.ap-northeast-2.amazonaws.com/user.png')

    # 유저 생성 시 필수 입력 사항
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'nickname']

    def __str__(self):
        return '{}'.format(self.nickname)
