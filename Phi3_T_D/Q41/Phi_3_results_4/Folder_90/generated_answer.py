def identical_elements(list1, list2):
    start_index = 262
    end_index = 746
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size.')
    return set(list1[start_index:end_index]) & set(list2[start_index:end_index])