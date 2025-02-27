from itertools import combinations

def find_subset_of_length_n(elements):
    return sum((1 for subset in combinations(elements, 10)))