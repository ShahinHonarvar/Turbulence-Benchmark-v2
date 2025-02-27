def identical_elements(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list) or len(list1) != len(list2):
        raise ValueError('Invalid input arguments')
    identical_elements_set = set()
    for i in range(len(list1)):
        if list1[i] in list2:
            identical_elements_set.add(list1[i])
    return identical_elements_set