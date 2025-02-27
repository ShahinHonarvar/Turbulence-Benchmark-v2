def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    shared_elements = set(list1[37:77]) & set(list2[37:77])
    return shared_elements