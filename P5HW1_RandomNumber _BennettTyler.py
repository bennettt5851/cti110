# This program will generate a random number for the user to guess
# 4/24/21
# CTI-110 P5HW1 - Random Number
# Tyler Bennett
#

import random
def main():

    print('MAIN MENU')
    print()
    print('-' * 13)
    print()
    print(' 1) Play Game')
    print(' 2) Exit')
    print(' What would you like to do? (Enter "Play Game" or "Exit"):', end ='')
    choice = input()
    if choice == 'Play Game':
        num = random.randint(1, 100)
        while True:
            print('Guess a number between 1 and 100:', end = '')
            guess = input()
            i = int(guess)
            if i == num:
                print('Congratulations!!!')
                print('Would you like to play again? (1 - yes, 2 - no):', end = '')
                choice = input()
                if choice == 'no':
                    print('Goodbye.')
                    break
                elif choice == 'yes':
                    num = random.randint(1, 100)
                    while True:
                        print('Guess a number between 1 and 100:', end = '')
                        guess = input()
                        i = int(guess)
                        if i == num:
                            print('Congratulations!!!')
                            print('Would you like to play again? (1 - yes, 2 - no):', end = '')
                            choice = input()
                            if choice == 'no':
                                print('Goodbye.')
                                break
                            
                            
                        elif i < num:
                            print('Too low, try again.')
                        elif i > num:
                            print('Too high, try again.')
            elif i < num:
                print('Too low, try again.')
            elif i > num:
                print('Too high, try again.')
    elif choice == 'Exit':
        print('Goodbye.')
main()


    
