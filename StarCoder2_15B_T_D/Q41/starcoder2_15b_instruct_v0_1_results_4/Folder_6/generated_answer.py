def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    identical_elements_set = set()
    for i in range(10, 67):
        if list1[i] in list2:
            identical_elements_set.add(list1[i])
    return identical_elements_set