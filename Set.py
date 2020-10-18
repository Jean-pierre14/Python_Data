thisSet = {"apple", "mac", "samsung", "hp proBook 440"}

# To Add new item
thisSet.add("Congo DRC")

# To Update our Set using Update
thisSet.update(["Apple 12", "Mac IOS", "Samsang 11 edge", "HP ProBook 440"])

# Loop through the Set using the for loop
print("_______________")
for x in thisSet:
    print(x)

# Display all the list
print("_______________")
print("To remove a specific item using remove method")
print("______________________________________________")
thisSet.remove("Apple 12")
print("We can also remove item using discard()")
print("________________________________________")
thisSet.discard("Mac IOS")
print("Every methods are able to work with our set Pop, clear, remove, del")
print(thisSet)
print(len(thisSet))

# Join of to sets
print("___________________________________")
print("To join to sets using union methods")
print("___________________________________")
SecondSet = {"one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine", "ten"}
join = thisSet.union(SecondSet)
print(join)
print(len(join))

# To update the elements of our set
thisSet.update(SecondSet)
print(thisSet)
print("NB: Union and update will exclude any duplicate items")
