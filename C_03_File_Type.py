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

# main routing goes here
while True:
    file_type = get_filetype()

    # if the user chose 'i', ask if they mean image or integer
    if file_type == 'i':

        want_image = input('Press [ENTER] for an integer or any key for an image. ')
        if want_image == '':
            file_type = 'integer'
        else:
            file_type = 'image'

    print(f'The file type is {file_type}')


    if file_type == 'xxx':
        break