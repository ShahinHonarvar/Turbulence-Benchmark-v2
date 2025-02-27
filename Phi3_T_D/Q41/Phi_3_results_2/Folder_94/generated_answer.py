def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 41:
        return set()
    return set(list1[28:41]) & set(list2[28:41])