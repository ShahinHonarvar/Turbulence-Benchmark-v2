from itertools import combinations

def find_subset_of_length_n(elements):
    n = 630
    num_elements = len(elements)
    if n > num_elements:
        return 0
    count = 0
    for subset in combinations(elements, n):
        count += 1
    return count