def identical_elements(list1, list2):
    if len(list1) == len(list2):
        return {x for i in range(5) for x in [list1[i], list2[i]] if x in list1 and x in list2}
    return set()