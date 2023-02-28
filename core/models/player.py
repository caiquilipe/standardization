from django.db import models

from core.constants import WalletChoices


class PlayerModel(models.Model):
    name = models.CharField(max_length=20)
    wallet = models.OneToOneField(
        "core.WalletModel",
        on_delete=models.PROTECT,
        limit_choices_to={"type": WalletChoices.REAL},
    )

    @classmethod
    def get_players(cls):
        return cls.objects.all()
