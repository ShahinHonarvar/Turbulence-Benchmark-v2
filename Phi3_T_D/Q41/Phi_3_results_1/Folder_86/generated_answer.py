def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    common_elements = set(list1[31:35]) & set(list2[31:35])
    return common_elements