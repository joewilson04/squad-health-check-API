from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.contrib.auth.models import User,Group

class scrumMasterGroup(Group):
    '''creates scrum master group'''
    def scrum_master_group(self):
        created = Group.objects.get_or_create(name='Scrum Master')

class userManager(BaseUserManager):
    '''manages all users'''

    def create_scrum_master(self, email, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email)

        user.set_password(password)
        scrum_master_group()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        '''create and save superusers'''


        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
