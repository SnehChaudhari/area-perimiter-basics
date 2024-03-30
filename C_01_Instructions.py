# generates headings (eg: ----- Heading -----)
def statement_generator(statement, decoration):
    print(f'\n{decoration * 5} {statement} {decoration * 5}')


# displays instructions
def instructions:
    statement_generator('Instructions', '-')

    print('''
instructions go here:
1. 
2. 
3. 
etc.
    ''')

# main routing goes here
want_instructions = input('Press [ENTER] to see the instructions or any key to continue.')
if want_instructions == '':
    instructions()

print('Program Continues...')