from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
from water.models import ApartmentCategory

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email' #Set the USERNAME_FIELD -- which defines the unique identifier for the User model -- to email
    REQUIRED_FIELDS = []

    objects = CustomUserManager() # Specified that all objects for the class come from the CustomUserManager

    # owned_apartments = models.ManyToManyField(ApartmentCategory)

    def __str__(self):
        return self.email


