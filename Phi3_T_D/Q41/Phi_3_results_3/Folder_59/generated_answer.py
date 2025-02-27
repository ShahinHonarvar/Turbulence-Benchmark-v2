def identical_elements(list1, list2):
    return set((x for x in list1[:9] + list2[:9] if x in list1[:9] and x in list2[:9]))