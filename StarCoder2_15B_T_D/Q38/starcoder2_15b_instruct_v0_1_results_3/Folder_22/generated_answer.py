def find_subset_of_length_n(elements):
    n = 72
    if len(elements) < n:
        return 0
    subsets = []
    for i in range(len(elements) - n + 1):
        subset = set()
        for j in range(i, i + n):
            subset.add(elements[j])
        subsets.append(subset)
    return len(subsets)