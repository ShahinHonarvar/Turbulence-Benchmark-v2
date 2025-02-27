def identical_elements(list1, list2):
    return {x for i, x in enumerate(list1[26:53]) if x in list2[26:53]}