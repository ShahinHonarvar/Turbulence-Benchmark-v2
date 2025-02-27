def find_subset_of_length_n(elements):
    """
    Calculates the number of subsets of size 300 of a given set.
    """

    def helper(idx, curr_size, curr_subset):
        if curr_size == 300:
            nonlocal num_subsets
            num_subsets += 1
            return
        if idx == len(elements):
            return
        helper(idx + 1, curr_size + 1, curr_subset + [elements[idx]])
        helper(idx + 1, curr_size, curr_subset)
    num_subsets = 0
    helper(0, 0, [])
    return num_subsets