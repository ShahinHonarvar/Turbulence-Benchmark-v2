def identical_elements(list1, list2):
    common_elements = {list1[i] for i in range(667, 775) if list1[i] in list2[667:775]}
    return common_elements