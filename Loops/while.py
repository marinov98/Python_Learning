numbers = 1

while numbers <= 1500:
    if numbers % 2 == 0:
        print(numbers)
    numbers += 1

L = []

while len(L) < 3:
    name = input("Please add a new name").strip().capitalize()
    L.append(name)
