def identical_elements(list1, list2):
    assert len(list1) == len(list2), 'Lists must be of the same size'
    assert all((isinstance(item, int) for item in list1 + list2)), 'Lists must contain only integers'
    return set(list1[43:52]) & set(list2[43:52])