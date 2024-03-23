# Ask the user for width and loop until they
# enter a number that is more than 0
def num_check(question):


    error = 'Please enter a number that is more than zero\n'
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than 0
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine starts here

keep_going = ''
while keep_going == '':
    # get width and height (and number check)
    width = num_check('Enter width: ')
    height = num_check('Enter height: ')
    cost = num_check('Enter cost per metre: ')

    # calculate the perimeter and price for the fence
    perimeter = 2 * (width + height)
    price = perimeter * cost
    # display output
    print()
    print(f'Perimeter: {perimeter} units)
    print(f'Price: {price:.2f}')
    # ask the user if they want to keep going
    keep_going = input('Press enter to keep going or press any key to quit. ')
    print()

print('Thank you for using my program.')
