def identical_elements(list1, list2):
    common_elements = {item for idx, item in enumerate(list1[310:371]) if item in list2[310:371]}
    return common_elements