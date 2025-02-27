import itertools

def find_subset_of_length_n(elements):
    length = 68
    return sum((1 for subset in itertools.combinations(elements, length)))