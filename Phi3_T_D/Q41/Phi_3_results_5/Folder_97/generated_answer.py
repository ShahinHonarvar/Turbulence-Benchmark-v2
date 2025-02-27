def identical_elements(list1, list2):
    common_elements = {x for i in range(40, 81) for x in [list1[i], list2[i]] if x in list1[40:81] and x in list2[40:81]}
    return common_elements