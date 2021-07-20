import random
number=random.randint(0, 5)
guess=random.randint(0, 5)
game=[number, guess]
print(game)
if(number==guess):
    print("You win!")
else:
    print("You lose!")