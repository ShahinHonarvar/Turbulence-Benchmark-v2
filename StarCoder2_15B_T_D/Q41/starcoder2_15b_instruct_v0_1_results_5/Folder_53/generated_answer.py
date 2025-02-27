def identical_elements(list1, list2):
    return {element for element in set(list1) & set(list2) if list1.count(element) > 1 and list2.count(element) > 1}