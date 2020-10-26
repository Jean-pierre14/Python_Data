a = 200
b = 250
c = 201
# if a > b:
# print("A is great than B")
# elif a > c:
# print("A is great than C")
# elif c > a:
# print("C is great than A")
# else:
# print("A is less than B")

if a < b:
    print("B is great than A")
else:
    print("A is great than B")

# Short hand if
a = 33
b = 33
c = 20

print("A") if a < b else print("=") if a == b else print("B")

# AND
if a == b and c > b:
    print("Both are true")
else:
    print("One is incorrect or both")

# NestedIf
if a == b:
    if c > b:
        print("A == B and C > B")
    else:
        print("B is great than C")
else:
    print("A is not egal to B")
