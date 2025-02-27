def identical_elements(list1, list2):
    overlap = {list1[i] for i in range(28, 41) if list1[i] in list2[28:41]}
    return overlap