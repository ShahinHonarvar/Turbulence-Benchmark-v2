def find_subset_of_length_n(elements):
    n = 91
    if len(elements) < n:
        return 0
    subsets = []

    def generate_subsets(elements, subset):
        if len(subset) == n:
            subsets.append(subset)
        else:
            for i, element in enumerate(elements):
                generate_subsets(elements[i + 1:], subset + [element])
    generate_subsets(elements, [])
    return len(subsets)