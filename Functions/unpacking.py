l = [1, 2, 3, 4, 5]

print(*l)  # unpacking iterable data types
# output: 1 2 3 4 5


print(*"abc")  # can unpack strings
# output: a b c


def add(x,y):
    return x + y


#  *args
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return(total)


add(1, 2, 3, 4, 5, 6, 7, 8, 9)


def about(name, age, likes):
    sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
    return(sentence)


dictionary = {"name": "Ziyad", "age": 23, "likes": "Python"}

about(**dictionary)  # Same as:
about(name="Ziyad", age=23, likes="Python")


def foo(**kwargs):
    for key in kwargs.items():
        print("{}:{}".format(key, value))

        
foo(huda="Female", ziyad="male")
#  output: ziyad:male
#          huda:Female
