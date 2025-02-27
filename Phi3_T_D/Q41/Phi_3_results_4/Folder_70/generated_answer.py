def identical_elements(list1, list2):
    if not (28 <= len(list1) and 28 <= len(list2)):
        raise ValueError('Lists must be of the same size and have a length of at least 29.')
    return set(list1[28:33]).intersection(set(list2[28:33]))