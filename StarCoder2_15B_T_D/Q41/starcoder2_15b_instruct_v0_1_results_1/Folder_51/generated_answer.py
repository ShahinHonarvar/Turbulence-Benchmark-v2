def identical_elements(list_1, list_2):
    if len(list_1) != len(list_2):
        raise ValueError('Lists must be of the same size')
    return set(list_1[0:3]) & set(list_2[0:3])