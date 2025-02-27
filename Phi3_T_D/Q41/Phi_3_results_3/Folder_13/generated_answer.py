def identical_elements(list1, list2):
    common_elements = set([item for item in set(list1[25:88]) if item in list2[25:88]])
    return common_elements