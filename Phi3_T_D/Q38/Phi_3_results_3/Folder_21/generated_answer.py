from itertools import combinations

def find_subset_of_length_n(elements):
    num_elements = len(elements)
    subsets = list(combinations(elements, 722))
    return len(subsets)