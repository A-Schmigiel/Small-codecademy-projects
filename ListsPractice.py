# create a list that consists of numbers 0-9 (inclusive)
single_digits = list(range(10))
squares = []
# create a for loop that prints out each digit
for digit in single_digits:
    print(digit)
    # append empty <squares> list to contain the squared value of each <digit>
    squares.append(digit ** 2)
print(squares)

# create list using list comprehension, each element is a <digit> to the third power
cubes = [digit ** 3 for digit in single_digits]
print(cubes)