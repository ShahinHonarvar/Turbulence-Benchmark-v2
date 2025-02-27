def identical_elements(list1, list2):
    set1 = set(list1[max(22, len(list1) - 1):min(89, len(list1))])
    set2 = set(list2[max(22, len(list2) - 1):min(89, len(list2))])
    return set1 & set2