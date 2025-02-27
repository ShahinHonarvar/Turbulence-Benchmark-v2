def identical_elements(list_1, list_2):
    if len(list_1) != len(list_2):
        return set()
    identical_elements_set = set()
    for i in range(len(list_1)):
        if list_1[i] in list_2[i] and 75 <= i <= 85:
            identical_elements_set.add(list_1[i])
    return identical_elements_set