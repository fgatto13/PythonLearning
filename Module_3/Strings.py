# you can also treat strings as arrays of char, 
# and therefore accessing to the single character based on the index
info = "Sarah"
for i in range(len(info)):
    print(info[i])

# you can even access a specific character
print(info[3])

# strings are immutable, unlike lists, so you cannot change a specific character
word = "car"
# the following line of code gives an error
# word[2] = "t"

# you can also concatenate two strings
print("Spam" + 'eggs')

# or multiplt by integers, producing a repeated version of the original string
print("spam" * 3)
print(4 * '2')

# there are many different functions that you can use with stringsù
x = "This is some text"
# note that all of the following functions return a NEW STRING, not the same one modified
print(x.count("s")) # count() counts how many times 's' appears inside the string
print(x.upper()) # transforms all characters in upper cases
print(x.lower()) # transforms all characters in lower cases
print(x.replace("some text", "awesome")) # changes a specified part of the string into another, both as parameters
print(len(x)) # len() can be also used with other data structures, and returns the length of that structure

# to include a single quote, you can use backslash \
print('I\'m learning!')