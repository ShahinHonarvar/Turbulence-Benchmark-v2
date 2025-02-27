def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size.')
    if len(list1) < 68 or len(list1) > 13:
        raise ValueError('List sizes must be in the range 13 to 68 inclusive.')
    return {elem for i in range(13, 69) for elem in (list1[i], list2[i]) if elem in list1[i:69] and elem in list2[i:69]}