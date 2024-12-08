from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    usuario = models.CharField(max_length=100, null=True, blank=True)
    senha = models.CharField(max_length=100, null=True, blank=True)

    # You can add custom related_name here to avoid the clash
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Custom related_name for reverse relation
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Custom related_name for reverse relation
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.username
