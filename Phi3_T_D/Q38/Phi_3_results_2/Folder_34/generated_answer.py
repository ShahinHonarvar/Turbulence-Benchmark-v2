def find_subset_of_length_n(elements):

    def count_subsets_of_n_from_start(subset_size, start, current_subset):
        if subset_size == 0:
            return 1
        if start >= len(elements):
            return 0
        count = 0
        for i in range(start, len(elements)):
            current_subset.append(elements[i])
            count += count_subsets_of_n_from_start(subset_size - 1, i + 1, current_subset)
            current_subset.pop()
        return count
    return count_subsets_of_n_from_start(97, 0, [])