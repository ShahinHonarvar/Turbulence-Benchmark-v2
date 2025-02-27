def identical_elements(list1, list2):
    temp_list1 = list1[62:93]
    temp_list2 = list2[62:93]
    return set(temp_list1) & set(temp_list2)