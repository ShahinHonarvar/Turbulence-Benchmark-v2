def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    common_elements = {element for index in range(80, min(201, len(list1))) for element in (list1[index], list2[index]) if element in list1 and element in list2}
    return common_elements