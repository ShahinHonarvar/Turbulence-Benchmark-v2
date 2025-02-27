def identical_elements(lst1, lst2):
    if len(lst1) < 7 or len(lst2) < 7:
        raise ValueError('Lists must have at least 7 elements each.')
    index_from = 7
    index_to = index_from + (len(lst1) - index_from)
    return set(lst1[index_from:index_to]) & set(lst2[index_from:index_to])