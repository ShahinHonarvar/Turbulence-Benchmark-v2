def identical_elements(list1, list2):
    return set([list1[2]]) & set([list2[2]]) if 2 < len(list1) and 2 < len(list2) else set()