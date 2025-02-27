def identical_elements(list1, list2):
    common_elements_set = {list1[i] for i in range(82, 87) if list1[i] in list2[82:87]}
    return common_elements_set