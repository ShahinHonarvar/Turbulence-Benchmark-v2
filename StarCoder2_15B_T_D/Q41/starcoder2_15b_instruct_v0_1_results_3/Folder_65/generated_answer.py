def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    result = set()
    for index, (element1, element2) in enumerate(zip(list1, list2)):
        if 56 <= index <= 98:
            if element1 in list2[index:]:
                result.add(element1)
            if element2 in list1[index:]:
                result.add(element2)
    return result