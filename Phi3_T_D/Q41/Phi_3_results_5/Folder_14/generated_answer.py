def identical_elements(list1, list2):
    common_set = {list1[i] for i in range(5, 8) if list1[i] in list2[5:8]}
    return common_set