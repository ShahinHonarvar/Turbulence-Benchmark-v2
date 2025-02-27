import itertools

def find_subset_of_length_n(my_set):
    subsets = itertools.combinations(my_set, 793)
    return len(list(subsets))