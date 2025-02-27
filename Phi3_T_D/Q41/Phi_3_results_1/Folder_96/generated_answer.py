def identical_elements(list_a, list_b):
    min_index, max_index = (50, 200)
    return set(list_a[min_index:max_index + 1]).intersection(list_b[min_index:max_index + 1])