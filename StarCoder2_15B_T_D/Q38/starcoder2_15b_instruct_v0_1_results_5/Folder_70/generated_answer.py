import itertools

def find_subset_of_length_n(set_of_elements):
    subsets = itertools.combinations(set_of_elements, 534)
    count = 0
    for subset in subsets:
        if len(subset) == 534:
            count += 1
    return count