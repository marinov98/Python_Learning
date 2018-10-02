word = "supercalifragilisticexpialidocious"

# slicing method: string[start:end:step]

# cali
print(word[5:9:1])

# fragil
print(word[9:15:1])

# califragilisticexpialidocious
print(word[5:])

# clfaiitcxildcos
print(word[5::2])

# superca
print(word[:7])

# super
print(word[:5])

# ---------------- negative -------------

# reverse
print(word[::-1])

# getting index from the back
# u
print(word[-2])

word.index("cali")  # gives 5 (the starting index)

# gives cali
print(word[word.index("cali"):word.index("fragi")])

# docious
print(word[word.index("docious"):])
