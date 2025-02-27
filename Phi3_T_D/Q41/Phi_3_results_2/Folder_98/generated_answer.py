def identical_elements(list1, list2):
    return {x for i, x in enumerate(list1[:6]) if x in list2[:6]}