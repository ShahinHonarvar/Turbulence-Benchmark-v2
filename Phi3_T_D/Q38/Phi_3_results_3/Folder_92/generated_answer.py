def find_subset_of_length_n(elements_set):
    length = 0
    subsets_count = {{}}
    for element in elements_set:
        subsets_count = subsets_count.update({element: length})
    return subsets_count['len(element)']