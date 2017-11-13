from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """ CUSTOM USER MODEL """
    def create_user(self, email, name, password=None):
        """ CREATE A NEW USER PROF OBJECT"""

        if not email:
            raise ValueError('Users must have an email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password) #encrypte password
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """ CREATES A SUPER USER INN SYTEM """
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

# Create your models here.

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Represent a user profile inside system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ USE TO GET NAME. """
        return self.name

    def get_short_name(self):
        """ USE TO GET SHORT NAME"""
        return self.name

    def __str__(self):
        """ CONVERT OBJ TO STRING """
        return self.email
