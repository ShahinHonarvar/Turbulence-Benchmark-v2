def identical_elements(list1, list2):
    assert len(list1) == len(list2), 'Lists must be of the same size'
    elements = {list1[i] for i in range(37, 52) if list1[i] in list2 and list2[i] in list1}
    return elements