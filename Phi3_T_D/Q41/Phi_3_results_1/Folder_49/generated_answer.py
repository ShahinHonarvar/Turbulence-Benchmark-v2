def identical_elements(list1, list2):
    shared_elements = set()
    for index in range(80, 201):
        if index < len(list1) and index < len(list2):
            if list1[index] in list2:
                shared_elements.add(list1[index])
    return shared_elements