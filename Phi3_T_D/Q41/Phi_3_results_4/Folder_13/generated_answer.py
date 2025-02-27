def identical_elements(list1, list2):
    return {element for element in set(list1[25:88]) if element in set(list2[25:88])}