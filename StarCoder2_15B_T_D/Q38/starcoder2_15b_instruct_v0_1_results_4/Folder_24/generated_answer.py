def find_subset_of_length_n(elements):
    subsets = []
    for element in elements:
        if len(subsets) == 74:
            return len(subsets)
        subsets.append(element)
    return len(subsets)