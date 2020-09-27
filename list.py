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
