def identical_elements(list1, list2):
    matching_elements = set(list1[2:]) & set(list2[2:])
    return matching_elements