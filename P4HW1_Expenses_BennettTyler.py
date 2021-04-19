# CTI-110 
# P4HW1 - Expenses 
# Tyler Bennett
# 3/28/21


#Prompt user to enter starting amount
def main():
    account = float( input('Enter starting amount in account $'))
    print('')

    moreExpenses = 'y'
    totalExpenses = 0
    i = 0
#Start a loop that asks user to enter expenses so long as they wish to continue
    while moreExpenses == 'y':
        userExpense = float( input('Enter expense: '))
        totalExpenses = totalExpenses + userExpense
        moreExpenses = input('Do you want to enter another expense?(y/n):')
        print('')
        i = i + 1
#If user wishes to end program, display original amount, num of expenses, and new amount
    if moreExpenses == 'n':
        print('Amount in account before expenses subracted $', account)
        print('Number of expenses entered:', i)
        print('Amount in account after expenses subracted is $', account - totalExpenses)
        
        
    
main()

    
    
