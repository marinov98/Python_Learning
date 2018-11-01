range(1,11) # make an iterable goes from 1 to 10

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numbers in range(1,1001): # prints 1000 numbers
    print(numbers)


for number in [1, 2, 3, 4]:
    print(number)


for letter in "abcd":
    print(letter)

for number in range(1,1001, 2): # going in steps of 2
    print(number)


vowels = 0
consonants = 0
    
for letter in "Hello":
    if letter.lower() in "aeiou":
        vowels += 1
    elif letter == "":
        pass
    else:
        consonants += 1

print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))


### part 2
students = {
    "male" : ["Tom", "Charlie", "Harry", "Frank"],
    "female" : ["Sarah", "Huda", "Samantha",
                "Emily", "Elizabeth"]
}


# prints all students that have "a" in their name
for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
