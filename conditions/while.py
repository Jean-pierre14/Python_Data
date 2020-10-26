i = 1

while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

for x in "banana":
print(x)

for x in range(6):
    print(x)

# Range start by 2 to 6 but not 6

for n in range(2, 6):
    print(n)

for m in range(2, 30, 3):
    print(m)

fruits = ["Apple", "Orange", "Violette"]
phones = ["iphones", "Samsung", "Techno"]

for f in fruits:
    for p in phones:
        print(f, p)
