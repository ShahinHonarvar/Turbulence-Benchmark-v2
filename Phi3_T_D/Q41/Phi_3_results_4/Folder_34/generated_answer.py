def identical_elements(list1, list2):
    start_index, end_index = (60, 200)
    return set(list1[start_index:end_index + 1]).intersection(list2[start_index:end_index + 1])