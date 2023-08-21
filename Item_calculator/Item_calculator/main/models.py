from django.db import models


class CharacterStats(models.Model):

    hp = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    attack = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    defense = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    speed = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    crit_rate = models.FloatField(
        null=False,
        blank=False,
    )

    crit_damage = models.FloatField(
        null=False,
        blank=False,
    )

    break_effect = models.FloatField(
        null=False,
        blank=False,
    )

    outgoing_healing_boost = models.FloatField(
        null=False,
        blank=False,
    )

    max_energy = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    energy_regeneration_rate = models.FloatField(
        null=False,
        blank=False,
    )

    effect_hit_rate = models.FloatField(
        null=False,
        blank=False,
    )

    effect_resistance = models.FloatField(
        null=False,
        blank=False,
    )

    physical_damage_boost = models.FloatField(
        null=True,
        blank=False,
    )

    fire_damage_boost = models.FloatField(
        null=True,
        blank=False,
    )

    ice_damage_boost = models.FloatField(
        null=True,
        blank=False,
    )

    lightning_damage_boost = models.FloatField(
        null=True,
        blank=False,
    )

    wind_damage_boost = models.FloatField(
        null=True,
        blank=False,
    )

    quantum_damage_boost = models.FloatField(
        null=True,
        blank=False,
    )

    imaginary_damage_boost = models.FloatField(
        null=True,
        blank=False,
    )

    physical_resistance_boost = models.FloatField(
        null=True,
        blank=False,
    )

    fire_resistance_boost = models.FloatField(
        null=True,
        blank=False,
    )

    ice_resistance_boost = models.FloatField(
        null=True,
        blank=False,
    )

    lightning_resistance_boost = models.FloatField(
        null=True,
        blank=False,
    )

    wind_resistance_boost = models.FloatField(
        null=True,
        blank=False,
    )

    quantum_resistance_boost = models.FloatField(
        null=True,
        blank=False,
    )

    imaginary_resistance_boost = models.FloatField(
        null=True,
        blank=False,
    )


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

    stat_line = models.OneToOneField(
        CharacterStats,
        primary_key=True,
        on_delete=models.CASCADE,
    )
