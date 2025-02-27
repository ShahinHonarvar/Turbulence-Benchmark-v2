def find_subset_of_length_n(elements):
    n = 60
    num_subsets = 1
    for e in elements:
        num_subsets *= len(elements) - n + 1
        elements.remove(e)
        n -= 1
    return num_subsets