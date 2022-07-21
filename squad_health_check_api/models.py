from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class staffManager(BaseUserManager):
    '''manages scrum masters and superusers'''

    def create_user(self, email, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        '''create and save superusers/scrum masters'''


        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        """Return string representation of our user"""
        return self.email
