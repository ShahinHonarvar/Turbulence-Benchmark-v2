def identical_elements(list1, list2):
    return set((l1 for i, l1 in enumerate(list1) if i >= 13 and i <= 68 and (l1 in list2)))