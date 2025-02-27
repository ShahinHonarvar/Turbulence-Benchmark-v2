def identical_elements(list1, list2):
    common_elements = {list1[i] for i in range(28, 39) if list1[i] in list2[28:39]}
    return common_elements