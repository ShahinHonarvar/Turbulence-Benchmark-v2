from itertools import combinations

def find_subset_of_length_n(elements):
    subsets_of_32 = [subset for subset in combinations(elements, 32)]
    return len(subsets_of_32)