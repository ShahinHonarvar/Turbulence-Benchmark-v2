def identical_elements(list1, list2):
    common_elements = {x for i, x in enumerate(list1[246:751]) if x in list2[246:751]}
    return common_elements