from itertools import combinations

def find_subset_of_length_n(elements_set):
    subsets = combinations(elements_set, 8)
    return len(list(subsets))