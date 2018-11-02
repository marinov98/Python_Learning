def about(name, age, likes="Python"):
    sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
    return sentence

# default values MUST be last (can be more than 1)
about("Jack", 23, "Python")
about(age = 23, name = "Jack", likes = "Python")

