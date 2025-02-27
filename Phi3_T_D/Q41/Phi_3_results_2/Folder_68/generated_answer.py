def identical_elements(list1, list2):
    common = set(list1[:8]) & set(list2[:8])
    return common