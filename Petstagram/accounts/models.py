from django.contrib.auth import models as auth_models
from django.contrib.auth.models import UserManager
from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram.accounts.managers import PetstagramUserManager
from Petstagram.common.validators import validate_only_letters


class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = PetstagramUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAXIMUM_LENGTH = 30

    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAXIMUM_LENGTH = 30

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do Not Show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAXIMUM_LENGTH,
        validators=(
            validate_only_letters,
            MinLengthValidator(FIRST_NAME_MIN_LENGTH)
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAXIMUM_LENGTH,
        validators=(
            validate_only_letters,
            MinLengthValidator(LAST_NAME_MIN_LENGTH)
        )
    )

    picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    email = models.EmailField(
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=(max([len(x) for x, _ in GENDERS])),
        choices=GENDERS,
        null=True,
        blank=True
    )

    user = models.OneToOneField(
        PetstagramUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'