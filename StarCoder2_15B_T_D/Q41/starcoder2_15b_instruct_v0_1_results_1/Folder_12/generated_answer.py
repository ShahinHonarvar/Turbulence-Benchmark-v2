def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    sublist1 = list1[14:65]
    sublist2 = list2[14:65]
    return set(sublist1) & set(sublist2)