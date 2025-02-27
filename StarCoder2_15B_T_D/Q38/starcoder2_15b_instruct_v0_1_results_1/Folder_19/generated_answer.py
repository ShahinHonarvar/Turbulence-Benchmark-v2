def find_subsets(set_of_elements, size):
    if size == 0:
        return [[]]
    if len(set_of_elements) == 0:
        return []
    element = set_of_elements.pop()
    subsets_without_element = find_subsets(set_of_elements, size)
    subsets_with_element = find_subsets(set_of_elements, size - 1)
    for subset in subsets_with_element:
        subset.append(element)
    return subsets_without_element + subsets_with_element