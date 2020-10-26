def function(x):
    return 5 * x


# print(function(5))


def many(child1, child2, child3):
    print(child1, child2, child3)
    print("The youngest is " + child3)


def unknown(*kids):
    print("The youngest is " + kids[1])


unknown('Red', 'Bleu', 'Yellow', 'Orange')

many(child1="Grace", child2="Germain", child3="Adolf")
