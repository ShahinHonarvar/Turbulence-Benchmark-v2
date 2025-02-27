def identical_elements(list1, list2):
    return set((element for element in set(list1[533:606]) if element in set(list2[533:606])))