#Question 7:
from functools import reduce
given_sets = [[1, 2, 3, 4, 8], [2, 3, 8, 5, 6], [8, 4, 5, 3, 7], [6, 9, 8, 3], [9,
12, 3, 7, 6, 8, 4, 6, 21, 1, 6]]

out=set(given_sets[0]).intersection(*given_sets)
print("Output:",out)
