import datetime

from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Pet(models.Model):
    NAME_MAX_LENGTH = 30

    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'

    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH
    )

    type = models.CharField(
        max_length=max([len(x) for x, _ in TYPES]),
        choices=TYPES
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    class Meta:
        unique_together = ('user', 'name')


class PetPhoto(models.Model):
    photo = models.ImageField(
        # validators=(
        #     # validate_file_max_size_in_mb(5)
        # )
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    publication_date = models.DateTimeField(
        auto_now=True
    )

    likes = models.IntegerField(
        default=0
    )

    tagged_pets = models.ManyToManyField(
        Pet
        # validate atleast one pet
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
