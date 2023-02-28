from django.db import models

from core.constants import WalletChoices


class WalletModel(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.IntegerField(choices=WalletChoices.choices)
