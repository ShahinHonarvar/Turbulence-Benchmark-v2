def identical_elements(list1, list2):
    common_elements = {list1[i] for i in range(50, 55) if i < len(list1) and list1[i] in list2[i]}
    return common_elements