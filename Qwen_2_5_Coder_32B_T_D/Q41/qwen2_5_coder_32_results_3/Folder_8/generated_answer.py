def identical_elements(list1, list2):
    return set() if len(list1) <= 23 or len(list2) <= 23 else {list1[23]} & {list2[23]}