def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    common_elements_set = set(list1[42:87]) & set(list2[42:87])
    return common_elements_set