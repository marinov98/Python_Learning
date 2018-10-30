A = [1, 2, 3]
A = A + list("BCD") # this works but ints would not works
A = A + list(str(123))
A = A + [[5,6, 7, 8, [5, 6, 7, 8], [10, 11, 12, 13]]

A.insert(2,[10, 20, 30]) # insert list at index 2
