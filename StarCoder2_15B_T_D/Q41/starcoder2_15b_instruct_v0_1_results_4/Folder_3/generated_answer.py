def identical_elements(list1, list2):
    sublist1 = list1[62:93]
    sublist2 = list2[62:93]
    return set(sublist1).intersection(set(sublist2))