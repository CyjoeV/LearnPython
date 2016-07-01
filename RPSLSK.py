import random

def name_to_number(name):
    if   name == "Rock":     return 0
    elif name == "Spock":    return 1
    elif name == "Paper":    return 2
    elif name == "Lizard":   return 3
    elif name == "Scissors": return 4
    else:
        print("Error:Invalid Name")


def number_to_name(number):
    if   number == 0:   return "Rock"
    elif number == 1:   return "Spock"
    elif number == 2:   return "Paper"
    elif number == 3:   return "Lizard"
    elif number == 4:   return"Scissors"
    else:
        print("Error:Invalid Number")


def rpsls(name):
    player_number = name_to_number(name)
    print("Player chooses",name)

    computer_number = random.randrange(0,5)
    computer_name = number_to_name(computer_number)
    print("Computer chooses",computer_name)

    diff = (computer_number - player_number) % 5
    if diff == 0: print("Its a Tie!")
    elif diff <= 2: print("Computer Wins!")
    elif diff > 2: print("Player Wins!")
    return ()

rpsls("Scissors")

