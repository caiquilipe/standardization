from rest_framework import serializers
from core.models.player import PlayerModel
from core.models.wallet import WalletModel
from core.serializers.wallet import InsertWalletSerializer


from django.db import transaction


class PlayerSerializer(serializers.ModelSerializer):
    wallet = InsertWalletSerializer()

    class Meta:
        model = PlayerModel
        fields = "__all__"

    def create(self, validated_data: dict):
        with transaction.atomic():
            validated_data.update(
                {"wallet": WalletModel.objects.create(**validated_data.pop("wallet"))}
            )
        return super().create(validated_data)
