def myFunction():
    print("Hello wold")
    print("____________")


myFunction()

# Argument


def greetting(name):
    print(name + " How are you?")


greetting("Grace")
greetting("Bisimwa")
greetting("|_______________Genuis Team___|")

# Default value of our argument


def par(country="Congo"):
    print("My country is " + country)


par("Goma")
par()


def food(foods):
    for x in foods:
        print(x)


foods = ["apple", "orange", "Tomato"]

food(foods)
