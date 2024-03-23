# Ask the user for the width and height
# (assume they put in valid data)
width = int(input('Enter width: '))
height = int(input('Enter height: '))

# calculate the area / perimeter
area = width * height
perimeter = 2 * (width + height)
# output the area and perimeter
print()
print(f'The area is {area} square units')
print(f'The perimeter is {perimeter} units')