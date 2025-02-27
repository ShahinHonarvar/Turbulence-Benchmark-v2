from itertools import combinations

def find_subset_of_length_n(elements):
    subsets_of_size_n = [subset for subset in combinations(elements, 63)]
    return len(subsets_of_size_n)