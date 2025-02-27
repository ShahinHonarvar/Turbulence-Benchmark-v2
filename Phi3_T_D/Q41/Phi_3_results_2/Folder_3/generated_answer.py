def identical_elements(list1, list2):
    return set([elem for i, elem in enumerate(list1[62:93]) if elem in list2[62:93]])