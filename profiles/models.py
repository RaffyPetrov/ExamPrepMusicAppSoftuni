from django.db import models
from django.core.validators import MinLengthValidator

from profiles.validators import AlphaNumericValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            AlphaNumericValidator(),
        ]
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
