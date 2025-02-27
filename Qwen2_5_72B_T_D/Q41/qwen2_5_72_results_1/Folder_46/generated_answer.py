def identical_elements(list1, list2):
    subset1 = set(list1[30:88])
    subset2 = set(list2[30:88])
    return subset1.intersection(subset2)