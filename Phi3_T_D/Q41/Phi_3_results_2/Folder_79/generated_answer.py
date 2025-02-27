def identical_elements(list1, list2):
    sub_list1 = set(list1[4:5])
    sub_list2 = set(list2[4:5])
    return sub_list1.intersection(sub_list2)