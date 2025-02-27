from itertools import combinations

def find_subset_of_length_n(elements_set):
    count = 0
    for subset in combinations(elements_set, 73):
        count += 1
    return count