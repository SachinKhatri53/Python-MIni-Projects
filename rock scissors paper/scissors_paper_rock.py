import random
import fontstyle
valid_response_as_no = ['N', 'n']

print("---------------------------------------------------")
print('\n')
print("\t\tROCK SCISSORS PAPER")
print('\n')
print("\tWelcome to the game")
print("\tPress any key to start or (N/n) to exit")
initiate = input("Your choice: ")
print("---------------------------------------------------")
if(initiate in valid_response_as_no):
    print('\n')
    print(fontstyle.apply("\t\tBye Bye..", "BOLD/RED_BG"))
    print('\n')
    print("___________________________________________________")
    exit()
else:
    valid_choice = [1, 2, 3]
    valid_options = {
        '1': 'Rock',
        '2': 'Scissors',
        '3': 'Paper'
    }
    while True:
        print(fontstyle.apply('\tWin 2 rounds', 'BOLD/BLUE_BG'))
        print('What do you choose?')
        print("\t(1.Rock, 2.Scissors, 3.Paper)")
        print(fontstyle.apply('Enter 0 to exit.', 'YELLOW'))
        counter = 0
        user_counter = 0
        opponent_counter = 0
        i = 1
        while counter < 2:
            random_choice = random.randint(1, 3)
            choice = input("Pick: ")
            choice = int(choice)
            if(choice == 0):
                print("___________________________________________________")
                print('\n')
                print(fontstyle.apply("\t\tBye Bye..", "BOLD/RED_BG"))
                print('\n')
                print("___________________________________________________")
                exit()
            elif(choice not in valid_choice):
                print(fontstyle.apply('Please enter valid choice.', 'YELLOW'))
                i -= 1
            else:
                print(fontstyle.apply("You chose: ", "BLUE") + valid_options[str(choice)])
                print(fontstyle.apply("Opponent chose: ", "RED") + valid_options[str(random_choice)])
                if(choice == random_choice):
                    print(fontstyle.apply("\tRound " + str(i) + " is a tie.", 'CYAN'))
                elif((choice == 1 and random_choice == 2) or (choice == 2 and random_choice == 3) or (choice == 3 and random_choice == 1)):
                    user_counter += 1
                    counter = user_counter
                    print(fontstyle.apply('\tYou won round ' + str(i), 'GREEN'))
                else:
                    opponent_counter += 1
                    counter = opponent_counter
                    print(fontstyle.apply('\tOpponent won round ' + str(i), 'RED'))
            i += 1
            counter == counter
        print("\n")
        if(user_counter > opponent_counter):
            print(fontstyle.apply("\t\tCongratulations. You Won", 'BOLD/GREEN_BG'))
        else:
            print(fontstyle.apply("\t\tOops! Opponent Won.", "BOLD/RED_BG"))
        print("\n")
        print("---------------------------------------------------")