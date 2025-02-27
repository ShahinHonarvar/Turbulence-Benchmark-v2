def identical_elements(list1, list2):
    return {x for i, x in enumerate(list1[:7]) if x in list2[:7]}