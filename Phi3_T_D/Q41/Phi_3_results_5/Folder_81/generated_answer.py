def identical_elements(list1, list2):
    if not (10 <= len(list1) <= 100 and 10 <= len(list2) <= 100):
        return set()
    set1 = set(list1[10:101])
    set2 = set(list2[10:101])
    return set1 & set2