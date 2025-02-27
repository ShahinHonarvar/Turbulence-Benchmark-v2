def identical_elements(list1, list2):
    common = {elem for elem in list1[246:751] if elem in list2[246:751]}
    return common