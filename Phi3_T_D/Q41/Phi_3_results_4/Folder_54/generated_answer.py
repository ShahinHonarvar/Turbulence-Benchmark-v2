def identical_elements(list1, list2):
    common_elements = {item for index, item in enumerate(list1[34:56]) if item in list2[34:56]}
    return common_elements