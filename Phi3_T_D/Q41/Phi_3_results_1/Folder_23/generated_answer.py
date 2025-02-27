def identical_elements(list1, list2):
    common_elements = set()
    for index in range(52, 72):
        if index < len(list1) and index < len(list2):
            if list1[index] == list2[index]:
                common_elements.add(list1[index])
    return common_elements