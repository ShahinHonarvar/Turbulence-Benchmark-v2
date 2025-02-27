def identical_elements(list1, list2):
    matching_elements = set()
    for index in range(74, 96):
        if index < len(list1) and index < len(list2) and (list1[index] == list2[index]):
            matching_elements.add(list1[index])
    return matching_elements