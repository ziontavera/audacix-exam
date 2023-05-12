from django.urls import path

from game_app.api.views import GameView

urlpatterns = [
    path("new/", GameView.as_view(), name="new_game"),
    path("<int:game_id>/", GameView.as_view(), name="current_game_state"),
    path("<int:game_id>/guess/", GameView.as_view(), name="guess_word"),
]
