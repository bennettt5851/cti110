
    

# This program allows user to add or subtract random numbers
# 4/25/21
# CTI-110 P5HW2 - Math Quiz
# Tyler Bennett
#
    #import random module & set up random numbers
import random

num_1 = random.randint(1, 500)
num_2 = random.randint(1, 500)
    #create function
def math_quiz():
    print('Welcome to Math Quiz')
    print('')
    print('MAIN MENU')
    print('-' * 20)
    print('1. Addition Random Numbers')
    print('2. Subtract Random Numbers')
    print('3. Exit')
    print('')
    print('Please choose one of the menu options:', end = '')
    choice = int(input())
    #use if loops to determine action after user input
    if choice == 1:
        answer = num_1 + num_2
        print(num_1)
        print('+', num_2)
        print('')
        print('Enter answer:', end = '')
        guess = int(input())
        guess_num = 1
    #use while until loop to keep loop going until user input is correct
        while guess != answer:
            if guess < answer:
                print('Sorry, guess is too low.')
                print('Try again:', end = '')
                guess = int(input())
                guess_num = guess_num +1
            elif guess > answer:
                print('Sorry, guess is too high.')
                print('Try again:', end = '')
                guess = int(input())
                guess_num = guess_num +1
    #Congratulate user after correct input
    #Display number of guesses
    #Repeat function
        print('Congratulations!!!! Your answer is correct.')
        print('Number of guesses:', guess_num)
        print('')
        math_quiz()
    #Repeat earlier steps for elif loop
    elif choice == 2:
        answer = num_1 - num_2
        print(num_1)
        print('-', num_2)
        print('')
        print('Enter answer:', end = '')
        guess = int(input())
        guess_num = 1
        while guess != answer:
            if guess < answer:
                print('Sorry, guess is too low.')
                print('Try again:', end = '')
                guess = int(input())
                guess_num = guess_num +1
            elif guess > answer:
                print('Sorry, guess is too high.')
                print('Try again:', end = '')
                guess = int(input())
                guess_num = guess_num +1
        print('Congratulations!!!! Your answer is correct.')
        print('Number of guesses:', guess_num)
        print('')
        math_quiz()
    elif choice == 3:
        print('Thank you for playing!')
        print('Bye!')
    #if user selcets choice to exit, terminate program
        
    
        
                
            
           

math_quiz()



