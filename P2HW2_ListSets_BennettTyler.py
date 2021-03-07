# This program will manipulate data in a list based off of user input
# CTI-110 
# P2HW2 - List and Sets 
# Tyler Bennett
# 3/7/21
#

numlist = []
print('Enter 10 numbers into the list:')
n = 10
for i in range(0, n):
    ele = int(input())
    numlist.append(ele)
    print(numlist)
    
print('Lowest number:', min(numlist))
print('')
print('Highest number:', max(numlist))
print('')
print('Total of numbers:', sum(numlist))
print('')
print('Average of numbers:', sum(numlist)/len(numlist))
print('')
num_set = set(numlist)
print('Here is the list in set form:', num_set)


# Display a prompt asking users to input 10 numbers
# Create a list function collecting 10 integers from user input
# Display lowest integer in list
# Display highest integer in list
# Display sum of integers in list
# Display average of integers in list
# Display the list in set form

