def identical_elements(list1, list2):
    common_elements = {element for element in list1[62:79] if element in list2[62:79]}
    return common_elements