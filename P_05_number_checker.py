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

# Main Routing Goes Here
for item in range(0, 2):
    width = num_check('Width: ')
    print (width)

print()

for item in range(0, 2):
    width = num_check('Height: ')
    print(height)
