def identical_elements(list1, list2):
    common_elements = {elem for idx, elem in enumerate(list1[209:557]) if elem in list2[209:557]}
    return common_elements