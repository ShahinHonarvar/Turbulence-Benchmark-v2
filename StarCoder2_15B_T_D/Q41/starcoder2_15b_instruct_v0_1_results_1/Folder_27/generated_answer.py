def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    identical_elements_set = set()
    for i in range(len(list1)):
        if list1[i] in list2[i] and 66 <= i <= 93:
            identical_elements_set.add(list1[i])
    return identical_elements_set