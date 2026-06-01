from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager


class Teacher(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='teacher_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='teacher_permissions'
    )

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"
