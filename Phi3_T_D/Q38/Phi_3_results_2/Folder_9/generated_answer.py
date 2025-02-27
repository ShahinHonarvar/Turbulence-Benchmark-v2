from itertools import combinations

def find_subset_of_length_n(elements_set):
    count = len(list(combinations(elements_set, 24)))
    return count