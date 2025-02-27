def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    identical_set = set()
    for i in range(12, 93):
        if list1[i] in list2:
            identical_set.add(list1[i])
    return identical_set