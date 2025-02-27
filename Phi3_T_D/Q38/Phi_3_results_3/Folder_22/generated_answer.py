def find_subset_of_length_n(elements):
    n = 72
    total_subsets = 0

    def count_subsets(index, selected):
        nonlocal total_subsets
        if len(selected) == n:
            total_subsets += 1
            return
        for i in range(index, len(elements)):
            count_subsets(i + 1, selected + [elements[i]])
    count_subsets(0, [])
    return total_subsets