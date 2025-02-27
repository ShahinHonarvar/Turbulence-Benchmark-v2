from itertools import combinations

def find_substs_of_length_n(elements_set):
    return sum((1 for _ in combinations(elements_set, 63)))