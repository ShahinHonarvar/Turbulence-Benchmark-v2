def identical_elements(list1, list2):
    if not list1 or not list2 or len(list1) != len(list2):
        return set()
    return set(list1[533:606]) & set(list2[533:606])