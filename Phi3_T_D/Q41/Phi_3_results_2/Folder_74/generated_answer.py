def identical_elements(list1, list2):
    common_elements = {item for i in range(17, 79) for item in [list1[i], list2[i]] if item in list1[17:79] and item in list2[17:79]}
    return common_elements