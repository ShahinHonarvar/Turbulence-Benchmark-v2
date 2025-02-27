def identical_elements(list1, list2):
    subset = set(list1[56:58] + list2[56:58])
    return {element for element in subset if element in list1[56:58] and element in list2[56:58]}