import random

class GuessingGame:

    def __init__(self, answer):
        self.answer = answer
        self.solved = False
            
    def solved(self):
        return self.solved

    # def guess(self, user_guess):
    #     self.user_guess = user_guess
    #     if user_guess == self.answer:
    #         return "Correct"
    #     elif user_guess < self.answer:
    #         return "Low"
    #     else:
    #         return "High"
        
        
# ----- DRIVER CODE -----
game = GuessingGame(random.randint(1,10))
# game = GuessingGame(10)

user_guess = int(input("Pick a number: "))

while game.solved is False:
    if user_guess != game.answer:
        print("Wrong Answer!")
        game.solved = False
        user_guess = int(input("Pick a number: "))
    else:
        print(f"Correct...Your guess was {user_guess} and the number was {game.answer}")
        game.solved = True

    
