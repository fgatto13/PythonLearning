# in this module, I'm learning how to use type conversion

print("insert first number: ")

# by default, input() returns a string, 
# therefore to get the desired type, we need to use type conversion functions:
# int, str, float
new_number = int(input())

# using a comma allows for concatenation of multiple strings (print converts its parameters in strings)
print("number iserted: ", new_number)

print("insert second number: ")
number_two = int(input())
print("number inserted: ",number_two)

# an if-else statement combined with comparisons and logical operators (and, or)
# allows to have a cleaner code and to make condition-based decisions 
if new_number > number_two:
    # a for loop allows to iterate multiple times over a specific set of instructions,
    # but it differs from C, C++ because using range() specifies how many times the index (i) 
    # has to be incremented, and therefore the number of iterations
    for i in range(number_two):
        print(new_number+i)
else:
    for i in range(new_number):
        print(number_two+i)
# clearly, there is no need to use parenthesis, though the code has to be well indented 
# and the set of instructions goes after the colon symbol: