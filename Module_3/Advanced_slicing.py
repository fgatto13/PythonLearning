# slicing can be used with strings too
plane = "airplane"
print(plane[0:3])
# expected output: "air"
print(plane[3:8])
# expected output: "plane"
# you can also specify only the end of the slice, so that it starts from the first element of the collection
print(plane[:5])
# or you can specify only the starting index, so that it slices from that onwards 
print(plane[3:])

# you can also use negative values with slicing, so that the greater index is the far right element
# check out the negativeSlicing.png image to understand better
animals = ["cat", "dog", "bird", "cow"]
print(animals[-1]) # Last element
print(animals[-2]) # Second last element
print(animals[-3:]) # Last 3 elements
print(animals[-3:-1])

# you can also combine positive and negative index
c = ['$', '£', '€', '¥']
print(c[1:-1])

# and since lists are mutable
c = ['$', '£', '€', '¥']
c[:2] = ['₣', '฿']
print(c)

brands = ["Honda", "Toyota", "BMW", "Mercedes"]
print(brands[-3:-1])