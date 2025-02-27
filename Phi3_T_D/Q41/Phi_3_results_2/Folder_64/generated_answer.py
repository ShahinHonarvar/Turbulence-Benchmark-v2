def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    common_elements_subset = set(list1[:4]) & set(list2[:4])
    return common_elements_subset