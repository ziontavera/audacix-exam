from django.db import models


class Game(models.Model):
    word = models.CharField(max_length=10)


class GameState(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game")
    state = models.CharField(max_length=10)
    word_state = models.CharField(max_length=10)
    allowed_wrong_answers = models.PositiveSmallIntegerField()
    wrong_answers = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
