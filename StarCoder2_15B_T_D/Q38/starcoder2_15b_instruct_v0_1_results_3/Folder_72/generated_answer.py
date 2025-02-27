def find_subset_of_length_n(elements):
    subsets = []
    for i in range(len(elements)):
        for subset in combinations(elements, i + 1):
            subsets.append(subset)
    return len([subset for subset in subsets if len(subset) == 16])