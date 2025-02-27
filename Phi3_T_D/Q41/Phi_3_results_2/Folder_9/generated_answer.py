def identical_elements(list1, list2):
    min_index, max_index = (max(70, len(list1) - 1), min(200, len(list1) - 1))
    return set(list1[min_index:max_index + 1]).intersection(list2[min_index:max_index + 1])