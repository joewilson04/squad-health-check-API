from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class userManager(BaseUserManager):
    '''manages all users'''

    def create_scrum_master(self, email, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        '''create and save superusers'''


        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

    def create_squad_member(self, email):
        if not email:
            raise ValueError("You must enter a valid email address")

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.save(using=self._db)
        return user
