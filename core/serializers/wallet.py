from rest_framework import serializers
from core.models.wallet import WalletModel
from core.constants import WalletChoices


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletModel
        fields = "__all__"


class InsertWalletSerializer(WalletSerializer):
    def validate_type(self, value):
        if value == WalletChoices.BONUS:
            raise serializers.ValidationError(detail="Type invalid.")
        return value
