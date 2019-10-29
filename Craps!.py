# Troy Jeffrey Amegashie
# 22 October 2019
# Craps Program

import random


def create():
    print("To start the game, add money to your bank.")
    print("How much would you like to add as your initial bankroll?\n>")
    return int(input())


def user_bet():
    print(f"How much would you like to bet from your bank on this round?\n>")
    return int(input())


def roll_dice():
    roll = random.randint(2, 12)
    print(f"You have rolled a {roll}")
    return roll


def play_game():
    bank = create()
    bet = user_bet()
    roll = roll_dice()
    if roll == 7 or roll == 11:
        print("You win!")
        bank = bank + bet
        print(f"You now have {bank}")
    elif roll == 2 or roll == 3 or roll == 12:
        print("You lost.")
        bank = bank - bet
        print(f"You now have {bank}")
    else:
        print(f"You have {roll} points, you need to roll {roll} to win.")
        points = roll
        roll = random.randint(1, 12)
        if roll == points:
          bank = bank + bet
          print(f"You won! You rolled {roll}.You now have {bank} in your bank")
        else:
          bank = bank - bet
          print(f"You lost. You rolled {roll}. You have {bank} in your bank")
          print("Would you like to play again? Y or N?")
          decision = input()
          if decision == "Y":
            play_game()
          else:
           print("Bye Bye. Thanks for playing.")


play_game()
