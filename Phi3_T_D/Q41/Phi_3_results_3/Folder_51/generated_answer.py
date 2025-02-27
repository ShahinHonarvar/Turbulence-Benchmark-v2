def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    else:
        return set([elem for elem in list1[:3] if elem in list2[:3]])