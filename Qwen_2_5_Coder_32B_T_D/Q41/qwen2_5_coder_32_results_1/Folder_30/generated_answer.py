def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    start, end = (max(55, 0), min(98, len(list1) - 1))
    set1 = set(list1[start:end + 1])
    set2 = set(list2[start:end + 1])
    return set1.intersection(set2)