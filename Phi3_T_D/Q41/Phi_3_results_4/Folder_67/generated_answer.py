def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 51 or len(list2) < 51:
        return set()
    return set(list1[22:51]).intersection(set(list2[22:51]))