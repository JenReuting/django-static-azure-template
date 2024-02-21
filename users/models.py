from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import BaseUserManager, AbstractUser

from core.models import UUIDBaseModel


class CustomUserManager(BaseUserManager):
    """
    Custom user manager for handling user creation and management.

    This class defines methods for creating regular users and superusers,
    as well as for retrieving users based on their natural key.
    """
    def normalize_email(self, email):
        """
        lowercase the entire email address
        """
        email = super().normalize_email(email)
        local, domain = email.rsplit('@', 1)
        email = '@'.join([local.lower(), domain])

        return email

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and returns a new user with the given email and password.
        """

        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and returns a new superuser. Ensures that is_staff and is_superuser
            are set to True.
            """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

    def get_by_natural_key(self, email):
        """
        Retrieves a user based on a natural key, which is the normalized email in this case.
        """
        normalized_email = self.normalize_email(email)
        return self.get(**{self.model.USERNAME_FIELD: normalized_email})


class CustomUser(AbstractUser, UUIDBaseModel):
    username = None

    email = models.EmailField(
        # Unique email for user authentication.
        _('email address'),
        max_length=255,
        unique=True
    )

    phone_number = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Phone Number",
    )

    profile_photo = models.ImageField(
        upload_to="profile_photos",
        blank=True,
        null=True,
        verbose_name="Profile Photo",
    )

    # Field used for logging in (set to 'email').
    USERNAME_FIELD = 'email'

    # Additional required fields for user creation.
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ['email']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
