## travis security project
known_users = ["Alice", "Bob", "Claire", "Dan"
               , "Emma", "Fred", "Georgie", "Harry"]

print(len(known_users))

while True:
    print("Hi my name is Travis")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ")
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print(" Your name remains stored")
    else:
        print("{} NOT recognized".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print(" Very well")          
# for deleting
L = [1, 2, 3, 4, 5]
del L[0]
example = ["A", "B", "C", "A", "B"]
del example[3]
del example[0:2]
