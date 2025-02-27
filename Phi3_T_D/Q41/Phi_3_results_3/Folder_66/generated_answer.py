def identical_elements(list1, list2):
    if len(list1) < 55 or len(list2) < 55:
        return set()
    set1 = set(list1[50:55])
    set2 = set(list2[50:55])
    return set1.intersection(set2)