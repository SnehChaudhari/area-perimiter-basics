# Ask the user for width and loop until they
# enter a number that is more than 0

error = 'Please enter a number that is more than zero\n'
while True:

    try:
        width = float(input('Width: '))

        if width > 0:
            break
            print(error)

    except ValueError:
        print(error)