def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size.')
    sliced_list1 = list1[29:80]
    sliced_list2 = list2[29:80]
    return set(sliced_list1) & set(sliced_list2)