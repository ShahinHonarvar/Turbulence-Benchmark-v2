from itertools import combinations

def find_subset_of_length_n(elements):
    n = 19
    count = 0
    for subset in combinations(elements, n):
        count += 1
    return count