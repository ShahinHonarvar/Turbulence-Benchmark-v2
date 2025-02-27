import itertools

def find_subset_of_length_n(elements):
    n = 74
    return sum((1 for combination in itertools.combinations(elements, n)))