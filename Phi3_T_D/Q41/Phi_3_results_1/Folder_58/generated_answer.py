def identical_elements(list1, list2):
    common_elements = {x for i, x in enumerate(list1[209:557]) if x in list2[209:557]}
    return common_elements