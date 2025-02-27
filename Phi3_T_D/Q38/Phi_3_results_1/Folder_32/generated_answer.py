from itertools import combinations

def find_subset_of_length_n(element_set):
    n = 22
    element_list = list(element_set)
    subset_count = len(list(combinations(element_list, n)))
    return subset_count