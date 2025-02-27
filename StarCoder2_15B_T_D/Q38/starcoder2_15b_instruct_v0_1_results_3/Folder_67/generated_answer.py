def find_subset_of_length_n(elements):
    subsets = []
    for element in elements:
        subset = {element}
        subsets.append(subset)
    return len(subsets)