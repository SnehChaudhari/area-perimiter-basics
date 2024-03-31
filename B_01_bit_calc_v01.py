# generates headings (eg: ----- Heading -----)
def statement_generator(statement, decoration):
    print(f'\n{decoration * 5} {statement} {decoration * 5}')


# displays instructions
def instructions():
    statement_generator('Instructions', '-')

    print('''
instructions go here:
1. 
2. 
3. 
etc.
    ''')




# asks users for file type (integer / image / text / XXX)
def get_filetype():

    #check for i or the exit code
    while True:
        response = input('Please enter file type: ').lower()

        # check for 'i' or the exit code
        if response == 'xxx' or response == 'i':
            return response

        # check if its an integer
        elif response in ['integer', 'int']:
            return 'integer'

        # check if its an image
        elif response in ['image', 'picture', 'img']:
            return 'image'

        # check for text
        elif response in ['text', 'txt', 't']:
            return 'text'

        # if the response is invalid, output an error
        else:
            print('Please enter a valid file format.')

# Ask the user for width and loop until they
# enter a number that is more than 0
def int_check(question, low):


    error = f'Please enter a number that is more than or equal to {low}\n'
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than 0
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# calculates how many bits are needed to represent an integer
def image_calc():
    # get image dimensions
    width = int_check('Width: ', 1)
    height = int_check('Height: ', 1)

    # calculate the number of pixels and multiply by 24 to get the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # set up an answer and return it
    answer = (f'Number of pixels: {width} x {height} = {num_pixels}'
              f'\nNumber of bits: {num_pixels} x 24 = {num_bits}')

    return answe



# calculates how many bits are needed to represent an integer
def integer_calc():
    # ask the user to enter an integer (more than or equal to 0)
    integer = int_check('Integer: ', 0)
    width = int_check('Width: ', 1)
    height = int_check('Height: ', 1)

    # convert the integer to binary and work out the number of bits needed
    raw_binary = bin(integer)

    # remove the leading '0b' from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)
    # set up an answer and return it
    answer = (f'{integer} in binary is {binary}.'
              f'\nWe need {num_bits} to represent it.')

    return answer



# calculates number of bits needed to represent text in ASCII
def calc_text_bits():

    # get text from user
    response = input("Enter text: ")
    # calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8
    # set up answer and return it
    answer = (f'{response} has {num_chars} characters.'
              f'\nWe need {num_chars} X 8 bits to represent it,'
              f'\nwhich is {num_bits} bits.')

    return answer




# main routing goes here

# display instructions if requested
want_instructions = input('Press [ENTER] to see the instructions or any key to continue.')
if want_instructions == '':
    instructions()


while True:
    file_type = get_filetype()

    if file_type == 'xxx':
        break

    # if the user chose 'i', ask if they mean image or integer
    if file_type == 'i':

        want_image = input('Press [ENTER] for an integer or any key for an image. ')
        if want_image == '':
            file_type = 'integer'
        else:
            file_type = 'image'

    if file_type == 'image':
        image_ans = image_calc()
        print(image_ans)
    if file_type == 'integer':
        integer_ans = integer_calc()
        print(integer_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)