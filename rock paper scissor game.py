# rock,paper,scissor game
import random
hand_signs = ['r', 'p', 's']

chance = 5
no_of_chance = 0
computer_point = 0
Your_point = 0

player_name = input("what your name?")
wanna_play = input("Hi, {}, welcome to the game,\nwould you like to play game then press enter".format(player_name))

print("\t \t \t \t Rock, Paper, Scissor Game\n \n")
print("r for Rock\np for Paper\ns for Scissor\n ")

while no_of_chance < chance:
    _input = input('\nRock,Paper,scissor:')
    _random = random.choice(hand_signs)

    if _input == _random:
        print("tie Both 0 points to each \n")

        # if user enter r
    elif _input == "r" and _random == "p":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_points is {computer_point} and your points {Your_point} \n")

    elif _input == "r" and _random == "s":
        Your_point = Your_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("You wins 1 point \n")
        print(f"computer_points is {computer_point} and your points {Your_point} \n")

        # if user enter p
    elif _input == "p" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_points is {computer_point} and your points {Your_point} \n")

    elif _input == "p" and _random == "r":
        Your_point = Your_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("You wins 1 point \n")
        print(f"computer_points is {computer_point} and your points {Your_point} \n")

    # if user enter s
    elif _input == "s" and _random == "r":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_points is {computer_point} and your points {Your_point} \n")

    elif _input == "s" and _random == "p":
        Your_point = Your_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("You wins 1 point \n")
        print(f"computer_points is {computer_point} and your points {Your_point} \n")

    else:
        print("you have input wrong \n")

    if computer_point == Your_point:
        print("Game Tie")

    elif computer_point > Your_point:
        print("computer win")

    else:
        print("You win")

        print(f"your points is {Your_point} and computer points is {computer_point}")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")
    print("Game over")


