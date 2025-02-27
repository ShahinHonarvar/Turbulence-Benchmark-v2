def identical_elements(list1, list2):
    sliced_list1 = set(list1[62:93])
    sliced_list2 = set(list2[62:93])
    return sliced_list1.intersection(sliced_list2)