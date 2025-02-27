from itertools import combinations

def find_subset_of_length_n(elements):
    count = 0
    subset_length = 74
    for subset in combinations(elements, subset_length):
        count += 1
    return count