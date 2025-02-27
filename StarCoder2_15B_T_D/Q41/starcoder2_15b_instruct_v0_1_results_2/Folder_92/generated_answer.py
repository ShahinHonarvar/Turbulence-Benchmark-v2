def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    identical_elements = set()
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            identical_elements.add(list1[i])
    return identical_elements