from itertools import combinations

def find_subset_of_length_n(set_of_elements):
    n = 59
    subsets = combinations(set_of_elements, n)
    return len(list(subsets))