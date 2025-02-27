def identical_elements(list1, list2):
    common_elements_set = set([list1[i] for i in range(10, 101) if list1[i] in list2[10:101]])
    return common_elements_set