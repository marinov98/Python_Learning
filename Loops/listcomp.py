# list thats contains even numbers from 1 - 100
even_numbers = [x for x in range(1,101) if x % 2 == 0]
# output: [2, 4, 6, ... 100]

# list of words
words = ["the" , "quick", "brown",
         "fox", "jumps", "over",
         "the", "lazy", "dog"]

# prints uppercase, lower case, the length of the string and
answer = [[w.upper(),w.lower(), len(w)] for w in words]
# output: [['THE','the', 3], ['QUICK', 'quick', 5]...etc

