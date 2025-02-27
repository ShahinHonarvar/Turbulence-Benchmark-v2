def identical_elements(list1, list2):
    return set([list1[2]]) & set([list2[2]]) if len(list1) > 2 and len(list2) > 2 else set()