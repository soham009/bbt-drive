from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_user(AbstractUser):
    '''Overrides the custom django user model'''
    # Datafields
    SUPER_ADMIN = 1
    ADMIN = 2
    MEMBER = 3
    ROLE_CHOICES = (
      (SUPER_ADMIN,'Super Admin'),
      (ADMIN,'Admin'),
      (MEMBER,'Member')
    )
    user_role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=ADMIN)
    updated_at = models.DateTimeField(auto_now=True)

class Member(models.Model):
    custom_user = models.ForeignKey(Custom_user, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.pk)