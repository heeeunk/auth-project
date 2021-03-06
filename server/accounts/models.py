from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from phonenumber_field.modelfields import PhoneNumberField

class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, email, phone, username, password=None):
        if not email:
            raise ValueError('no user email')
        if not phone:
            raise ValueError('no user phone')
        if not username:
            raise ValueError('no user username')
        user = self.model(
            email = self.normalize_email(email),
            phone = phone,
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 user 생성
    def create_superuser(self, email, username, phone=None, password=None):
        if phone is None:
            phone = 0
        user = self.create_user(
            email,
            password = password,
            phone = phone,
            username = username
        )
        user.is_admin = 1
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(default='', max_length=20, null=False, blank=False, unique=True)
    email = models.EmailField(default='', max_length=255, null=False, blank=False, unique=True)
    phone = models.IntegerField(default=0, null=False, blank=False, unique=True)
    is_active = models.IntegerField(default=0)    
    is_admin = models.IntegerField(default=0)
    
    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 username으로 설정
    USERNAME_FIELD = 'username'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['password', 'email', 'phone']

    def __str__(self):
        return self.username
