def identical_elements(list1, list2):
    range_len = min(200, len(list1)) - min(40, len(list1)) + 1
    return set(list1[min(40, len(list1)):min(200, len(list1)) + 1]).intersection(list2[min(40, len(list2)):min(200, len(list2)) + 1])