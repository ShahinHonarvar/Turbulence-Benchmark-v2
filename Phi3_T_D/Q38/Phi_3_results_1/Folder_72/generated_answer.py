from itertools import combinations

def find_subset_of_length_n(elements):
    n = 16
    subsets = combinations(elements, n)
    return len(list(subsets))