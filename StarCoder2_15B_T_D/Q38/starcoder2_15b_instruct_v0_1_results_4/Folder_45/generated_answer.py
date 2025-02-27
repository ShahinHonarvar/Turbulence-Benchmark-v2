def find_subset_of_length_n(elements):
    n = 3
    return len(set((tuple(sorted(elements[i:i + n])) for i in range(len(elements) - n + 1))))