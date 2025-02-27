def identical_elements(list1, list2):
    return {x for x in list1[:5] if x in list2[:5]}