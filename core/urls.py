from django.urls import path

from core.views.player import PlayerView

urlpatterns = [path("players", PlayerView.as_view(), name="PlayerView")]
