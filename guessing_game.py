import random

class GuessingGame:
    
    def __init__(self, answer):
        self.answer = answer
        self.solved = False

    def guess(self, user_guess: int) -> str: #ensure method only returns a string
        if user_guess < self.answer:
            self.solved = False
            return 'low'
        if user_guess > self.answer:
            self.solved = False
            return 'high'
        self.solved = True
        return 'correct'

    def is_solved(self) -> bool: #ensure method only returns boolean value
        return self.solved

#---Driver code---
game = GuessingGame(random.randint(1, 10))
last_guess = None
last_result = None

while not game.is_solved():
    if last_guess is not None:
        print(f"Oops! Your last guess ({last_guess}) was {last_result}.\n")

    try:
        user_input = input("Enter your guess: ") #prompt user for input
        guess = int(user_input) #convert input to integer and assign it to 'guess' variable
    except ValueError: #if user_input is not an number then print error message
        print("PLEASE ENTER ONLY A NUMBER.\n")
        continue 

    last_guess = guess 
    last_result = game.guess(guess)
    print(last_result) 

print(f"{last_guess} was correct!") 


