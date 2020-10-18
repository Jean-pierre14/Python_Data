list = ["item 1", "item 2", "item 3", "item 4", "item 5", "item 6"]
# list[6] = "item 7"
print(list[-1])
print(list[1:5])

print(len(list))

for x in list:
    print(x)

if 'item 1' in list:
    print('Yes it is in')
else:
    print('No does not')

list.append("Added")
list.insert(1, "Pikipiki")
print(list)

# To remove an element within the list
# remove()
list.remove('item 1')
print(list)
# pop do the same thing like remove method
list.pop()
print(list)

# del is the method that remove only the index of the list, let me show an example
del list[0]
print(list)
# it can delete all the list like so
del list
print(list)


# Clear, this method clear all items of the list
# list.clear()

# this copy method help to copy the list
myList = list.copy()
print(myList)
