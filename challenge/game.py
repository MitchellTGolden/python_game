from fighter import Fighter
from robot import Robot
from ent import Treant
from pirate import Pirate
from ninja import Ninja
import random

bender = Robot('Bender', 10, 5, 10, 50, "Hey")
walle = Robot('Walle', 10, 5, 10, 50, "Walllllll EEEE")
groot = Treant('Groot', 10, 5, 10, 50, "I am Groot")


def charcreate():
    charList = ["Robot=1", "Ninja=2", "Treant=3", "Pirate=4"]
    valinput = 0
    while valinput == 0:
        for i in range(len(charList)):
            print(charList[i])
        inpNum = input()
        if inpNum == '1':
            print('You chose Robot.')
            character_type = 'Robot'
            valinput = 1
        elif inpNum == '2':
            print('You chose Ninja.')
            character_type = 'Ninja'
            valinput = 2
        elif inpNum == '3':
            print('You chose Treant')
            character_type = 'Treant'
            valinput = 3
        elif inpNum == '4':
            print('You chose Pirate')
            character_type = 'Pirate'
            valinput = 4
        else:
            print("That's not a valid input")
    print('What is your character name?')
    inpName = input()
    print("What is your character's saying?")
    inpSaying = input()
    health = random.randrange(200, 400)
    strength = random.randrange(30, 40)
    speed = random.randrange(30, 40)
    dexterity = random.randrange(20, 40)
    return eval(character_type + "('" + inpName + "'," + str(speed) + ',' + str(dexterity) + ',' + str(strength) + ',' + str(health) + ",'" + inpSaying + "')")

print("Welcome to the Thunderdome!")
# players = 0
# while players == 0:
#     selection = input()
#     if (selection == '1'):
#         players = 1
#     elif (selection == '2'):
#         players = 2
#     else:
#         print("You gotta pick 1 or 2")

print('Player 1, create your character:')
combatant1 = charcreate()
combatant1.displayInfo()

print('Player 2, create your character:')
combatant2 = charcreate()
combatant2.displayInfo()

# if players == 2:
#     print('Player 2, create your character:')
#     combatant2 = charcreate()
# else:
#     combatant2 = Treant('Groot', 45, 45, 45, 600, "I am Groot")
# combatant2.displayInfo()

def fight(attacker, defender):
    move = 0
    while move == 0:
        print(f"\n{attacker.name}'s turn:")
        print("choose your move: 1) attack, 2) special 3) heal 4) magic ")
        selection = input()
        if (selection == '1'):
            print(f"{attacker.name} attacks!")
            attacker.attack(defender)
            move = 1
        elif (selection == '2'):
            print(f"{attacker.name} uses their special attack!")
            attacker.special(defender)
            move = 2
        elif (selection == '3'):
            print(f"{attacker.name} heals!")
            attacker.heal(defender)
            move = 3
        elif (selection == '4'):
            print(f"{attacker.name} casts!")
            attacker.magic(defender)
            move = 4
        else:
            print("you gotta pick 1, 2, 3 or 4")
        # combatant1.damage(combatant2,20)


while combatant1.check_health() and combatant2.check_health():
    print(f"\n{combatant1.name} and {combatant2.name} are locked in combat!")
    fight(combatant1, combatant2)
    fight(combatant2, combatant1)
    # print('input quit to quit')
    # selection = input()
    # if (selection == 'quit' or 'QUIT' or 'Quit'):
    #     print("You quit!")
    #     break
    
print("thanks for playing")
