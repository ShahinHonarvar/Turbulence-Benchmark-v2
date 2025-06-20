from itertools import combinations

def find_subset_of_length_n(elements):
    subsets = combinations(elements, 31)
    return sum((1 for _ in subsets))