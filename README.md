# audacix-exam: Hangman Coding Exercise

## Definition of Done
1. Create Game with endpoint `game/new`
   - Game will contain random word in the list ["Hangman", "Python", "Audacix", "Bottle", "Pen"]
   - Should return game_id after creation
   
2. Show Game State with endpoint `game/:id`
   - Show state of the game with `InProgress` `Won` or `Loss` value
   - Show current state of the word. Default state of the word is all unguessed letters are replaced with underscores
   - Show allowed number of guesses the player will be making
      - Number of allowable guesses depends on the length of the word divided by 2
   - Show number of incorrect guesses the player has made
   - Should return JSON data

3. Update GameState with inputs from user with endpoint `game/{game_id}/guess`
   - Should be able to update the game state before returning
   - Show game state and guess result

## Tested with Postman
- All endpoints can be tested with Postman or something similar to postman tool


## URLS
1. http://127.0.0.1:8000/game/new/
2. http://127.0.0.1:8000/game/{game_id}/
3. http://127.0.0.1:8000/game/{game_id}/guess/


## Packages installed:
- Django
- DjangoRestFramework
