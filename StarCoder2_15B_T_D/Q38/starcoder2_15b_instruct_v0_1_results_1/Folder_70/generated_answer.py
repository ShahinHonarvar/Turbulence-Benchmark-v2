def find_subset_of_length_n(elements):

    def helper(elements, subset, n):
        if len(subset) == n:
            subsets.append(subset)
            return
        for i, element in enumerate(elements):
            helper(elements[i + 1:], subset + [element], n)
    subsets = []
    helper(elements, [], 534)
    return len(subsets)