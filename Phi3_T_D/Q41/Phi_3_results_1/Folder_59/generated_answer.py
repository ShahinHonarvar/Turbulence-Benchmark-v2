def identical_elements(list1, list2):
    common_elements = set(list1[:9]) & set(list2[:9])
    return common_elements