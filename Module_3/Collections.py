# a collection in Python is a series of elements contained in the same variable
# a collection is also an ordered set of items
list1 = ["car", "bus", "boat", "plane"]

# you can print the whole list 
print(list1)
# or you can print each element using a for loop
for x in list1:
    print(x)

# lists can also contain different data types
list2 = ["cats", 2]
# and you can access a specific item using its index
print(list2[0])

# you can also directly change an element of the list
# the reason being that lists are mutable, so you can change the values after they've been created
print("insert: ")
list2[0] = input()
print(list2[0])

# or store the value of a specified index inside another variable
new_variable = list2[0]

# also, you can define single variables and then define the list with these
name = "Sarah"
age = 24
user_info = [name, age]

# slicing allows to extract a portion of a list. 
# Let's say that you want to extract items from 1 to 3, here is how you do it
animals =["cat", "dog", "bird", "cow"]
print(animals[1:3])
# the output will be ['dog', 'bird'], because it'll extract all of the elements from index 1 to index 3
# the following will print the whole list
print(animals[0:4])
# while this is gonna print everything except 'cow'
print(animals[0:3])
# the starting index is inclusive. The stopping index is exclusive.