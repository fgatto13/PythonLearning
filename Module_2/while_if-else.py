# in this script, let's focus on how to use while loops
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

# again, using an if-else statement to make condition based decisions
if new_number < number_two:
    # here we use the while loop to iterate while the number is greater than 0
    # the difference with the for loop is that, in here, we do not specify how many times we iterate, 
    # but rather the condition(s) valid to iterate
    while new_number > 0:
        print(new_number)
        # this is a decrement functino 
        # Note: in python, ++ and -- do not work. Instead, you need to use += or -= 
        # to specify that the operation involves the assigned variable
        new_number -= 1
else:
    while number_two > 0:
        print(number_two)
        number_two -= 1