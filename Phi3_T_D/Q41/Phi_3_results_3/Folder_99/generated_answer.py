def identical_elements(list1, list2):
    return set([item for i, item in enumerate(list1[309:371]) if item in list2[309:371]])