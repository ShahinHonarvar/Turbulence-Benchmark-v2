def find_subset_of_length_n(elements):
    n = 8
    total_subsets = 1 << len(elements)
    count = 0
    for bitmask in range(total_subsets):
        subset = {elements[j] for j in range(len(elements)) if bitmask & 1 << j}
        if len(subset) == n:
            count += 1
    return count