# Ask user for name
name = input("What is your name?: ")
print(name)
# Ask user for age
age = input("What is your age?: ")
print(age)
# Ask user for city
city = input("What city do you live in: ")
print(city)
# Ask user for what they enjoy
love = input("What do you love doing: ")
# Create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}."
output = string.format(name, age, city, love)
# Print output to screen
print(output)

# "{}-{}".format(A,B) this will formate whatever data you put in whether it
# is string or not "{1}-{0}".format(A,B) A is 0, B is 1

# text.count(letter) counts the number of times the letter shows up
# .lower() and .upper() for lowercase and uppercase islower() and isupper for checking
# .istitle() for if its in titl format isdigit() to check for digits
# .isalnum (is alphanumeric) .isalpha() check for letters ONLY
# .index() for index .find() to find a specific part
# .strip() removes any instance of that index .lstrip() and .rstrip() for left or right
# name = input(something).strip() strips the spaces
# len(something) shows the length of the string
