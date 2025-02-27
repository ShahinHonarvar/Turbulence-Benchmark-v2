from itertools import combinations

def find_subset_of_length_n(set_of_elements):
    subsets = combinations(set_of_elements, 68)
    return len(list(subsets))