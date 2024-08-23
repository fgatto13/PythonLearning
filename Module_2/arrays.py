# in this script, we're learning how to use arrays in python

# let's start by reading the dimension from the input
print("insert array dimension:")
dim = int(input())

# let's now declare an array
array = []

# let's now iterate through the array to insert values
for i in range(dim):
    print("insert value at position ", i ,":")
    # append is used to insert a new element inside the array
    array.append(int(input()))
# the following for loop is used to print all of the elements inside the array
for x in array:
    print(x)
# we can also use conditional statements to check wether or not there is a specific element in the array
print("insert the number to search for:")
search = int(input())
# this is a common way to check the elements inside the array 
# without having to do an explicit search (unlike in C/C++)
if search in array:
    print(True)
else:
    print(False)