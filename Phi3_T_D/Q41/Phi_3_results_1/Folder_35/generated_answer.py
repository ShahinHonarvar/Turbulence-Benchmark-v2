def identical_elements(list1, list2):
    shared_elements = {element for element in set(list1[30:49]) if element in set(list2[30:49])}
    return shared_elements