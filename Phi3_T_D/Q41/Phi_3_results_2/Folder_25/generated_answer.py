def identical_elements(list1, list2):
    assert len(list1) == len(list2), 'Lists must be of the same size'
    range_start, range_end = (29, 93)
    return set(list1[range_start:range_end + 1]).intersection(list2[range_start:range_end + 1])