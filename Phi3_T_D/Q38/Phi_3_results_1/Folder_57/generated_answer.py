def find_subset_of_length_n(elements):

    def count_subsets(n, subset_size):
        if subset_size == 0 or n < subset_size:
            return 1
        return count_subsets(n - 1, subset_size) + count_subsets(n - 1, subset_size - 1)
    total_elements = len(elements)
    if total_elements < 92:
        return 0
    return count_subsets(total_elements, 92)