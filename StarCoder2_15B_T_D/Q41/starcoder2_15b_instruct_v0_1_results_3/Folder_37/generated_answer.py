def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    identical_elements_set = set()
    for i in range(1, len(list1) - 1):
        if list1[i] == list2[i]:
            identical_elements_set.add(list1[i])
    return identical_elements_set