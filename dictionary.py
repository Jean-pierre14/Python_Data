thisDictionary = {
    "name": "Grace",
    "sex": "Male",
    "skinColor": "Brown"
}
print(thisDictionary)

Name = thisDictionary['name']
print("To call a specific item we will use his name to do that")
print("________________________________________________________")
print(Name)
print("________________________________________________________")
print("We can use also the Get() method to call a specific item through our dictionary")
print("________________________________________________________________________________")
x = thisDictionary.get('sex')
print(x)

# To change the value

print("________________________________________________________")
print("To change value")

thisDictionary["skinColor"] = "Black"
print("________________________________________________________")
print(thisDictionary)
print("________________________________________________________")
print("Loop through a dictinary")
print("________________________________________________________")
for n in thisDictionary:
    print(n)
print("_____________________")
print("This will display all key name, now let us display the values")
for n in thisDictionary:
    print(n + ' :' + thisDictionary[n])

print("________________________________________________________")
print("But you can use this way also to display values .value()")
print("________________________________________________________")
for n in thisDictionary.values():
    print(n)


print("_________________________________")
print("to display once key with values")
print("_________________________________")
for x, y in thisDictionary.items():
    print(x+': ' + y)

print("You can check using if condition or made all other things like add")
# Add values
thisDictionary["color"] = "White"
print(thisDictionary)
if "Grace" in thisDictionary.values():
    print("Yes")
else:
    print("No")

# To Remove item using pop

thisDictionary.pop('name')
print(thisDictionary)
# this method remove the lastest item of the dictinary popitem
thisDictionary.popitem()
print(thisDictionary)

# Nested dictionary
myParent = {
    "identity": {
        "name": "Ushindi",
        "Sex": "Male",
        "Nationality": "Congolese"
    }, "Profession": {
        "name": "Piki piki community",
        "post": "CTO and cofounder"
    }
}
print(myParent)
print("________________________________________________________")
print("You can also get nested dictinaries that already exist like so")

child1 = {
    "name": "Grace",
    "age": 23
}
child2 = {
    "name": "Germain",
    "age": 19
}
child3 = {
    "name": "Adolf",
    "age": 17
}

nestedic = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(nestedic)


# Using the dict contructor to make a dictionary
thisdict = dict(name="Python", age=12)
print("Dictionary created using dist() ")
print(thisdict)
