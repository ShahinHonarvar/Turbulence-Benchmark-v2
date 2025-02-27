def identical_elements(list1, list2):
    common_elements = {list1[i] for i in range(30, 49) if list1[i] in list2 and list2[i] == list1[i]}
    return common_elements