from itertools import combinations

def find_subset_of_length_n(elements_set):
    n = 872
    subsets_count = 0
    for subset in combinations(elements_set, n):
        subsets_count += 1
    return subsets_count