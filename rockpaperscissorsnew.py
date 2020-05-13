# Rock Paper Scissors the game!
# To play this game type your name and the version of the game.
# in example if you want to play standard rock paper scissors, type only your name
# otherwise type formats like: rock,paper,scissors,lizard,spock
# game is not complet finished



import random
counter = 0
userscore = 0
x = 0
gameoptions = []
computer_list = []

file = open('rating.txt', 'r')

players = file.readlines()

playersname = input("Enter your name: ")
print("Hello, {}".format(playersname))
gameoptions = input().split(",")

if gameoptions == ['']:
    gameoptions = ['rock', 'paper', 'scissors']

for i in gameoptions:
    computer_list.append(i)
    
playerlist = []

for i in players:
    if playersname in i:
        x = i.split()
playerscore = x[1]
                
file.close()

userscore += int(playerscore)

def gameengine(computer_list, choice ,computer_choice,userscore):
    local_computer_list = []
    local_computer_list += computer_list
    choiceindex = local_computer_list.index(choice)
    local_computer_list.remove(choice)
    relationships = local_computer_list[choiceindex:] + local_computer_list[:choiceindex]
    seperator = len(relationships) / 2
    choice_beats = relationships[int(seperator):]
    choice_get_beaten = relationships[:int(seperator)]
            
    if computer_choice in choice_beats:
        print(win)
        userscore += 100
    elif computer_choice in choice_get_beaten:
        print(lose)
    elif computer_choice == choice:
        print(draw)
        userscore += 50
    return userscore


print("Okay, let's start")
while counter == 0:
    
    ran_num = random.randint(0, len(computer_list) - 1)
    computer_choice = computer_list[ran_num]

    lose = "Sorry, but computer chose " + computer_choice
    draw = "There is a draw " + "(" + computer_choice + ")"
    win = "Well done. Computer chose " + computer_choice + " and failed"
    
    choice = input()  
    
    if choice in computer_list:
        userscore = gameengine(computer_list, choice, computer_choice, userscore)
    elif choice == "!exit":
        counter += 1
    elif choice == "!rating":
        print(userscore)
    else:
        print("Invalid input")

print("Bye!")