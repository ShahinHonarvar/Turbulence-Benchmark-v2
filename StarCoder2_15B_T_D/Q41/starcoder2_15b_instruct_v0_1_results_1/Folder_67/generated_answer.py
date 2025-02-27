def identical_elements(list1, list2):
    list1_slice = list1[22:51]
    list2_slice = list2[22:51]
    return set(list1_slice).intersection(set(list2_slice))