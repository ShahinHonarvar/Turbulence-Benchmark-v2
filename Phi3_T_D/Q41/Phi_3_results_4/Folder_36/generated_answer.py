def identical_elements(list1, list2):
    common = {val for i, val in enumerate(list1) if 246 <= i <= 750 and val in list2[246:751]}
    return common