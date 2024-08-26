# the break statement is used to stop the loop when some condition is met.
# This is very useful when searching for a specific item or condition, 
# and there’s no need to continue once it’s found.
songs = ["hey jude", "yesterday", "strawberry field forever", "let it be"]

for song in songs:
    print("searching")
    if song == "yesterday":
        print("playing: " + song)
        break

# another example
prices = [10, 54, 9, 44, 6, 26, 15]
total = 0
for price in prices:
    total+=price
    print(total)
    if total > 100:
        print("Limit exceeded")
        break

# we can also use break to stop an endless loop
while True:
    print("insert a text (insert Stop to stop the program):")
    text = input()
    print(text)
    if text.lower() == 'stop':
        break

# The continue statement allows you to skip the current iteration of a loop 
# when a certain condition is true.
ages = [13,19, 22, 8, 75, 34, 26, 41]
for age in ages:
    if age < 18:
        continue
    print(age)

# You can use the continue statement with while loops.
# The code below will skip the iteration when the day number is 4
day_number = 0
while day_number <= 7:
    if day_number == 4:
        day_number += 1
        continue
    print("Turn on the lights!")
    day_number += 1   