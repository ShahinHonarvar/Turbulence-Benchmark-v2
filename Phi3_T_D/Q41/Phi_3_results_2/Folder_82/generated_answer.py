def identical_elements(list1, list2):
    common_elements_set = set(list1[20:201]).intersection(set(list2[20:201]))
    return common_elements_set