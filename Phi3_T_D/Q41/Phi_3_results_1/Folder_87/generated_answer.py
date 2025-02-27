def identical_elements(lst1, lst2):
    if len(lst1) != len(lst2):
        raise ValueError('Lists must be of the same size')
    return set(lst1[36:47]) & set(lst2[36:47])