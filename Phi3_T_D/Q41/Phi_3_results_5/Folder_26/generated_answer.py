def identical_elements(list1, list2):
    set1 = set(list1[62:99 + 1])
    set2 = set(list2[62:99 + 1])
    return set1.intersection(set2)