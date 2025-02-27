def identical_elements(list1, list2):
    common_elements = set()
    for index in range(40, 201):
        if 0 <= index < len(list1) and 0 <= index < len(list2):
            if list1[index] in list2:
                common_elements.add(list1[index])
    return common_elements