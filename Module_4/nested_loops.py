# we can create nested loops inside python
arr1 = ["me", "you", "them"]
arr2 = ["inside", "outside"]
for i in arr1:
    print("whatever")
    for j in arr2:
        print(i + " " + j)


# we can use conditional operators to check if an item is inside a list
print("me" in arr1)

# or we can use them to check if a character appears in a string
print('o' in arr1[1])

# you can also combine if-else with loops
for i in arr1:
    if 'o' in i:
        print(i)
    else:
        for j in arr2:
            print(j)

# for instance, we can combine multiple operations
counter = 0
devices = ['PC', 'TV', 'PS', 'TV', 'PS', 'Xbox', 'TV']
for device in devices:
  if device == 'TV':
    counter = counter +1
print("Number of TVs:", counter)

# such as counting the number of times a character appears in a string
message = "You have a new message"
count = 0
for i in message:
  if i == 'a':
    count += 1
print(count)