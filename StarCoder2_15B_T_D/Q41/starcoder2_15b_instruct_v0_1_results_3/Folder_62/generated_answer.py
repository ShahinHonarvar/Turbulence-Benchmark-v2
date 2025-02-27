def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of equal size')
    return set(list1[91:100]).intersection(set(list2[91:100]))