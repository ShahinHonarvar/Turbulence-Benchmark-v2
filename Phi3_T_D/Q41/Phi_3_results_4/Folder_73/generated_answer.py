def identical_elements(list1, list2):
    range_start, range_end = (19, 92)
    return set(list1[range_start:range_end + 1]) & set(list2[range_start:range_end + 1])