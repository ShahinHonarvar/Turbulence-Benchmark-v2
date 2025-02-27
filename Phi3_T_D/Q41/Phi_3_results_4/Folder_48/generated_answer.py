def identical_elements(lst1, lst2):
    if len(lst1) != len(lst2):
        raise ValueError('Lists must be of same size')
    intersection = set(lst1[533:606]) & set(lst2[533:606])
    return intersection