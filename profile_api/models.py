from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.models import BaseUserManager

from django.conf import settings
# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for User Profile"""
    
    def create_user(self,email,name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("Users must have an email address")
        
        email=self.normalize_email(email)
        user = self.model (email=email,name=name)
        
        user.set_password(password)
        user.save(using=self.db)
        
        return user
    
    def create_superuser(self, email, name, password):
        """Create and save a new super user"""
        user =self.create_user(email, name, password)
        
        user.is_superuser= True;
        user.is_staff= True
        
        user.save(using= self.db)
    


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database Model for user in the system"""
    email= models.EmailField(max_length=255, unique=True)
    name= models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    
    objects : UserProfileManager = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['name']
    
    def get_full_name(self):
        """Retrieve full name of the user"""
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        """Represents string representation of our user"""
        return self.email
    
class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now= True)
    
    
    def __str__(self):
        """Return models as a string"""
        return self.status_text
    
    
    


