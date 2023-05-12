import random

from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from game_app.api.serializers import GameStateSerializer
from game_app.models import Game, GameState


class GameView(APIView):
    def post(self, request):
        with transaction.atomic():
            new_game = Game.objects.create(
                word=random.choice(
                    ["Hangman", "Python", "Audacix", "Bottle", "Pen"]
                ).lower()
            )

            GameState.objects.create(
                game_id=new_game,
                state="InProgress",
                word_state="_" * len(new_game.word),
                allowed_wrong_answers=round(len(new_game.word) / 2),
                wrong_answers=0,
            )

        return Response(
            {"message": "Success!", "game_id": new_game.id},
            status=status.HTTP_201_CREATED,
        )

    def get(self, request, game_id):
        game_state = get_object_or_404(GameState, game_id=game_id)
        serializer = GameStateSerializer(game_state)

        return Response(
            {"messgae": "Success", "game_state": serializer.data},
            status=status.HTTP_200_OK,
        )

    def put(self, request, game_id):
        game_state = get_object_or_404(GameState, game_id=game_id)
        word = game_state.game_id.word
        guess = request.data["input"].lower()
        result = None
        with transaction.atomic():
            if (
                "_" in game_state.word_state
                and game_state.wrong_answers < game_state.allowed_wrong_answers
            ):
                if guess in word:
                    result = "Correct"
                    for i in range(len(word)):
                        if guess == word[i]:
                            game_state.word_state = (
                                game_state.word_state[:i]
                                + guess
                                + game_state.word_state[i + 1 :]
                            )
                else:
                    result = "Incorrect"
                    game_state.wrong_answers += 1

            if "_" not in game_state.word_state:
                game_state.state = "Won"

            if game_state.wrong_answers == game_state.allowed_wrong_answers:
                game_state.state = "Loss"

            game_state.save()

        serializer = GameStateSerializer(game_state)

        return Response(
            {"guess_result": result, "game_state": serializer.data},
            status=status.HTTP_200_OK,
        )
