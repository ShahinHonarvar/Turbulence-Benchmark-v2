def identical_elements(list1, list2):
    slice1 = set(list1[31:73])
    slice2 = set(list2[31:73])
    return slice1 & slice2