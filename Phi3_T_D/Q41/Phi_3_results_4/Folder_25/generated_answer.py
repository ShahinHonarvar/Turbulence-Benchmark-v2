def identical_elements(list1, list2):
    result_set = {element for i in range(29, 94) for element in [list1[i], list2[i]] if element in list1 and element in list2}
    return result_set