import sys

print('''Fibonacci Sequence
      
The Fibonacci sequence begins with 0 and 1, and the next number is
the sum of the previous two numbers. The sequence continues forever:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987 . . .      
''')

while True:
    while True:
        print('Enter the Nth Fibonacci number you wish to calculate')
        print('(such as 5, 50, 1000, 9999), or QUIT to quit:')
        response = input('> ').upper()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response.isdecimal() and int(response) !=0:
            nth = int(response)
            break

        print('Please enter a number greater than zero, or QUIT.')
    print()

    if nth == 1:
        print('0')
        print()
        print('The #1 Fibonacci number is 0.')
        continue
    elif nth == 2:
        print('0, 1')
        print()
        print('The #2 Fibonacci number is 1.')
        continue

    if nth > 10000:
        print('WARNING: This will take a while to display on the screen.')
        print('If you want to quit this program before it is done,')
        print('press CTRL-C.')
        input('Press Enter to begin...')

    secondtolastnumber = 0
    lastnumber = 1
    fibnumberscalculated = 2
    print('0, 1, ', end="")

    while True:
        nextnumber = secondtolastnumber + lastnumber
        fibnumberscalculated +=1

        print(nextnumber, end='')

        if fibnumberscalculated == nth:
            print()
            print()
            print(f"The #{fibnumberscalculated} Fibonacci number is {nextnumber}")
            print()
            break

        print(', ', end='')

        secondtolastnumber = lastnumber
        lastnumber = nextnumber

