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
