def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 8:
        return set()
    return set(list1[1:9]) & set(list2[1:9])