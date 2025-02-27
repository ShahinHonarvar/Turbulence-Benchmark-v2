def identical_elements(list1, list2):
    start_index, end_index = (35, 49)
    intersection = set(list1[start_index:end_index + 1]) & set(list2[start_index:end_index + 1])
    return intersection