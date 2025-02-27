def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    sliced_list1 = set(list1[55:99])
    sliced_list2 = set(list2[55:99])
    return sliced_list1.intersection(sliced_list2)