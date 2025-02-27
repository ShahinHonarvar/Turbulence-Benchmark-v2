def identical_elements(list1, list2):
    return {element for element in set(list1[200:201]) if element in list2[200:201]}