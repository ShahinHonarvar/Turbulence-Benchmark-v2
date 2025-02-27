def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    shared_elements = set()
    for i in range(10, 101):
        if i < len(list1) and i < len(list2) and (list1[i] in list2):
            shared_elements.add(list1[i])
    return shared_elements