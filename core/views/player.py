from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from rest_framework import status

from core.serializers.player import PlayerSerializer
from core.models.player import PlayerModel

from core.utils.hande_errors import handle_error_serializer

from drf_yasg.utils import swagger_auto_schema


class PlayerView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses={200: PlayerSerializer})
    def get(self, request):
        return Response(
            data=PlayerSerializer(instance=PlayerModel.get_players(), many=True).data,
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        request_body=PlayerSerializer, responses={201: PlayerSerializer}
    )
    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(detail=handle_error_serializer(serializer.errors))
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
