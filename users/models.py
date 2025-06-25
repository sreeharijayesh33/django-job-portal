from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.validators import RegexValidator
import enum


# for two types of user roles jobseeker and employer
class RoleEnum(enum.Enum):
    JOBSEEKER = 'jobseeker'
    EMPLOYER = 'employer'

    @classmethod
    def choices(cls): # function returns values in of django, can use dropdown menu
        return [(tag.value, tag.value.capitalize()) for tag in cls]


# Creating a Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        if not full_name:
            raise ValueError("The Full Name must be set")
        email = self.normalize_email(email) #converts into lowercase
        
        #Creates a user instance
        user = self.model(email=email, full_name=full_name, **extra_fields)#extra_fields lets us pass more data like phone, role, etc.
        user.set_password(password) #sets password securely and hashes it
        user.save(using=self._db) #for saving the user to DB
        return user
    

#for admin related access
    def create_superuser(self, email, full_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True) #Ensures that the superuser has admin access
        extra_fields.setdefault('is_superuser', True)#Ensures that the superuser has admin access
        return self.create_user(email, full_name, password, **extra_fields)


# Custom User Model
class User(AbstractBaseUser, PermissionsMixin): #ABU-login and password fetaure, PM-admin related,groups permissions
    email = models.EmailField(unique=True) #login field
    full_name = models.CharField(max_length=255) 
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$')], #optional ph_no field with validation
        blank=True,
        null=True
    )
    role = models.CharField(max_length=20, choices=RoleEnum.choices()) #limited two choices
    is_verified = models.BooleanField(default=False) #whether user verified the email
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) #for users can't access admin panel

    objects = CustomUserManager() #links user-model with user-manager

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email
    

