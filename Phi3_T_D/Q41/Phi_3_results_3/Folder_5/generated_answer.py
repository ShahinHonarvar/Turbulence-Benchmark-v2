def identical_elements(list1, list2):
    return set(list1[8:10]) & set(list2[8:10]) if len(list1) >= 10 and len(list2) >= 10 else set()