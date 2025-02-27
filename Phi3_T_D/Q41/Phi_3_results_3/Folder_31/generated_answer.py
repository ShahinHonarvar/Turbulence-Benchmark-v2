def identical_elements(list1, list2):
    common_elements_set = {list1[i] for i in range(75, 89) if list1[i] in list2[75:89]}
    return common_elements_set