def identical_elements(list1, list2):
    if len(list1) < 75 or len(list1) > 94 or len(list2) < 75 or (len(list2) > 94):
        raise ValueError('Both lists must contain elements between index 75 and index 94.')
    return set((el1 for el1, el2 in zip(list1[74:95], list2[74:95]) if el1 == el2))