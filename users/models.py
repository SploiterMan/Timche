from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from extensions.dateJalali import django_jalali
from django.utils import timezone
from django.db import models
from .managers import *


class User(AbstractBaseUser, PermissionsMixin):
    firstName = models.CharField(max_length=55, verbose_name='نام')
    lastName = models.CharField(max_length=55, verbose_name='نام خانوداگی')
    phoneNumber = models.CharField(max_length=11, verbose_name='شماره مویابل', unique=True)
    email = models.EmailField(verbose_name='ایمیل', unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'lastName', 'phoneNumber']

    objects = UserManager()

    def __str__(self):
        return f'{self.firstName} {self.lastName}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def created_jdate(self):
        return django_jalali(self.date_joined)

    class Meta:
        verbose_name = 'حساب کاربر'
        verbose_name_plural = 'حساب کاربران'
