def identical_elements(list1, list2):
    assert len(list1) == len(list2), 'Lists must be of the same size'
    return set(list1[59:98]) & set(list2[59:98])