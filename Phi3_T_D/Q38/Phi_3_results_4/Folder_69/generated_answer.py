def find_subset_of_length_n(elements):

    def find_combinations(items, combo_size):
        if combo_size == 0:
            return [[]]
        if not items:
            return []
        return [[items[0]] + tail for tail in find_combinations(items[1:], combo_size - 1)] + find_combinations(items[1:], combo_size)
    subsets_of_length_n = find_combinations(list(elements), 894)
    return len(subsets_of_length_n)