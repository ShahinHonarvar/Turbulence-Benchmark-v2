from itertools import combinations

def find_subset_of_length_n(elements):
    n = 860
    combinations_list = list(combinations(elements, n))
    return len(combinations_list)