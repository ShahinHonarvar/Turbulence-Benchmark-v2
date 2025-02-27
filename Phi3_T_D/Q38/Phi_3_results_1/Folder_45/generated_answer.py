from itertools import combinations

def find_subset_of_length_n(elements):
    N = 33
    return len(list(combinations(elements, N)))