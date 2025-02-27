def identical_elements(list1, list2):
    common_elements = set(list1[56:67])
    common_elements.intersection_update(list2[56:67])
    return common_elements