def identical_elements(list1, list2):
    common_elements = {item for i in range(3, 6) for item in [list1[i], list2[i]] if item in list1 and item in list2}
    return common_elements