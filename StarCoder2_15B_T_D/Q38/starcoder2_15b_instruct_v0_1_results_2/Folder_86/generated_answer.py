import itertools

def find_subset_of_length_n(elements):
    subsets = itertools.combinations(elements, 380)
    count = 0
    for subset in subsets:
        if len(subset) == 380:
            count += 1
    return count