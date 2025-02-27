def identical_elements(list1, list2):
    assert len(list1) == len(list2), 'Lists must be of the same size'
    return set(list1[74:96]) & set(list2[74:96])