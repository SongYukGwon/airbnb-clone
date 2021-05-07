from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "Male"
    GENDER_FEMALE = "Female"
    GENDER_OTHER = "Other"

    GENDER_CHOICE = (
        (GENDER_MALE, "Male"),
        (GENDER_MALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLEISH = "En"
    LANGUAGE_KOREAN = "Kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLEISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "usd"), (CURRENCY_KRW, "krw"))

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES,
        max_length=2,
        blank=True,
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES,
        max_length=3,
        blank=True,
    )
    superhost = models.BooleanField(default=False)
