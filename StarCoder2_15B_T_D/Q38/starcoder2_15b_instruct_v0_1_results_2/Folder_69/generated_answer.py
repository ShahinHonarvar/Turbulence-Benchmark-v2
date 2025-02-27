def find_subset_of_length_n(elements):
    n = 894
    if len(elements) < n:
        return 0
    subsets = []

    def backtrack(subset, remaining_elements):
        if len(subset) == n:
            subsets.append(subset.copy())
            return
        for i, element in enumerate(remaining_elements):
            subset.append(element)
            backtrack(subset, remaining_elements[i + 1:])
            subset.pop()
    backtrack([], elements)
    return len(subsets)