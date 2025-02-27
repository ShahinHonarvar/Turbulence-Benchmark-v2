def identical_elements(list1, list2):
    assert len(list1) == len(list2), 'Lists must be of the same size'
    assert 0 <= 686 <= 987 < len(list1), 'Invalid indices'
    return set(list1[686:988]) & set(list2[686:988])