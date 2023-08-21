from django.db import models


class CharacterModels(models.Model):
    MAX_NAME_LEN = 75

    name = models.CharField(
        max_length=MAX_NAME_LEN,
    )

    avatar = models.ImageField(
        upload_to='avatars',
        null=False,
        blank=False,
    )