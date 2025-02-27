def identical_elements(list1, list2):
    return set([list1[6], list2[6]]) if 6 < len(list1) and list1[6] == list2[6] else set()