def identical_elements(list1, list2):
    return set([list1[23]]) & set([list2[23]]) if 0 <= 23 < len(list1) and 0 <= 23 < len(list2) else set()