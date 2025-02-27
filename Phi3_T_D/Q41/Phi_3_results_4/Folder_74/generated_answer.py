def identical_elements(list1, list2):
    shared = {element for element in list1[17:79] if element in list2[17:79]}
    return shared