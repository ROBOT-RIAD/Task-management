from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password):
        if not email:
            raise ValueError("please inser email")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using =self._db)
        return user
    
    def create_superuser(self,email,password):
        user =self.Create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using =self.db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    fullname = models.CharField(max_length=120,default=" ",blank=True,null=True)
    email = models.EmailField(max_length=150,unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email