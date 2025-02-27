def identical_elements(list1, list2):
    indices_range = slice(23, -3)
    return set(list1[indices_range]).intersection(list2[indices_range])