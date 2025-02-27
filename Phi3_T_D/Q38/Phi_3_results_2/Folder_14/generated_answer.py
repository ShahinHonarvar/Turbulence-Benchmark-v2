from itertools import combinations

def find_subset_of_length_n(elements, n=17):
    if len(elements) < n:
        return 0
    subsets = 0
    for combination in combinations(elements, n):
        subsets += 1
    return subsets