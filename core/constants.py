from django.db.models import IntegerChoices


class WalletChoices(IntegerChoices):
    BONUS = 0
    REAL = 1
