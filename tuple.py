tupley = ("Apple 1", "iphone 11", "Techno camon", "infinix", "sonic", "films")
# Display the element
# print(tupley)

# To display a specific value, or index
# print(tupley[0])

# It gonna start to the end of the tuple
# print(tupley[-1])

# To display the elements start to the thrid up to fiveth element
# print(tupley[2:5])

# To count the element of our tuple using count method
# print(len(tupley))

# Change Tuple Values
y = list(tupley)
print(y)

# New value to the index 0
y[2] = "Iphone 12 Pro"
x = tuple(y)
print(x)

# For loop thought our tuple

for n in tupley:
    print('item ' + n)

# Check thought the tuple if these as Iphone 12 Pro
if "Iphone 12 Pro" in x:
    print("Yes, 'Iphone 12 Pro' exist within our tuple")

# Join to tuple
newTuple = (1, 2, 3, 4)
joinTuples = newTuple + tupley
print(tupley)
print(newTuple)
print(joinTuples)

# Use tuple method
newTupleContructor = tuple(("new item", "new york", "new car", "new life"))
print(newTupleContructor)
