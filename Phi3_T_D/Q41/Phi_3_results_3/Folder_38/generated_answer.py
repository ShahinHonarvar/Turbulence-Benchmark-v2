def identical_elements(list1, list2):
    start, end = (22, 63)
    return {x for i, x in enumerate(list1[start:end + 1], start) if x in list2[start:end + 1]}