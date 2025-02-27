def identical_elements(list1, list2):
    relevant_slice = slice(32, 36)
    set1 = set(list1[relevant_slice])
    set2 = set(list2[relevant_slice])
    return set1.intersection(set2)