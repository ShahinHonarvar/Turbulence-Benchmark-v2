import itertools

def find_subset_of_length_n(elements):
    elements_list = list(elements)
    combinations = itertools.combinations(elements_list, 90)
    return len(list(combinations))