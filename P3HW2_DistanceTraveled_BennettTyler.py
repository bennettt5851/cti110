# CTI-110
# P3HW2 - Distance Traveled
# Tyler Bennett
# 3/15/21
# This program calculates distance traveled base on user input

def main():

    print("Enter car's speed:", end =" ")
    speed = int(input())
    print("Enter time traveled:", end=" ")
    time = int(input())

    if time <= 0:
        print('Error ! time entered should be >0')
    else:
        print('Speed entered:', speed)
        print('Time entered:', time)
        
    print('Distance Traveled', speed * time)


main()
main()
main()
main()
main()
main()

# Display "Ener car's speed:"
# Input car speed
# Display "Enter time traveled:"
# Input time traveled
# Display error message if input is < or = 0
# Display input values
# Set speed multiplied by time
