from itertools import combinations

def find_subset_of_length_n(elements):
    subsets = combinations(elements, 92)
    return sum((1 for _ in subsets))