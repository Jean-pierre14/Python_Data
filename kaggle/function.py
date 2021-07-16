def mainFunction():
    name = "Grace Bisimwa"
    # return name
    print(name)
mainFunction()

def EnterName(name):
    print(name + " Developer")

EnterName("Grace")
# EnterName("Mapendano")
# EnterName("Bahizi")
# EnterName("Peter")

def MyFunction(*Allnames):
    print("This is the name Two " + Allnames[1])

MyFunction("Adolf", "Daniel", "Espoire", "Esther")
# The submition of the computer to the boss

# Passing a list fo arguments
def foodF(food):
    for x in food:
        print(x)

fruits = ["Orange", "Tomate", "Mango"]
foodF(fruits)