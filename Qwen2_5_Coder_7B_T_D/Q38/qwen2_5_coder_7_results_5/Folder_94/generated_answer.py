def find_subset_of_length_n(elements):
    n = 93
    if n > len(elements):
        return 0
    return len(elements) ** n