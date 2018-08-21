# Write a function `create_array` that generates an array using some algorithm

# Your code here


def create_array(p):
    return [(i, pow(i, 3)) for i in range(1, p + 1)]


assert create_array(2) == [(1, 1), (2, 8)]
assert create_array(3) == [(1, 1), (2, 8), (3, 27)]
