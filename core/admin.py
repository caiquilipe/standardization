from django.contrib import admin
from core.models.player import PlayerModel
from core.models.wallet import WalletModel

# Register your models here.
admin.site.register(WalletModel)
admin.site.register(PlayerModel)
