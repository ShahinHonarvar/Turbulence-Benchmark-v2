from itertools import combinations

def find_subset_of_length_n(elements):
    count = 0
    n = 54
    for subset in combinations(elements, n):
        count += 1
    return count