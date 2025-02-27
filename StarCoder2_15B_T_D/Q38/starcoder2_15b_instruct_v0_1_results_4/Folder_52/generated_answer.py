def find_subset_of_length_n(elements):
    n = 32
    if len(elements) < n:
        return 0
    subsets = []

    def generate_subsets(current_subset, remaining_elements):
        if len(current_subset) == n:
            subsets.append(current_subset.copy())
            return
        for i in range(len(remaining_elements)):
            element = remaining_elements[i]
            current_subset.append(element)
            generate_subsets(current_subset, remaining_elements[i + 1:])
            current_subset.pop()
    generate_subsets([], elements)
    return len(subsets)