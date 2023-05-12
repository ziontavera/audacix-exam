from rest_framework import serializers

from game_app.models import GameState


class GameStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameState
        fields = ["state", "word_state", "allowed_wrong_answers", "wrong_answers"]
