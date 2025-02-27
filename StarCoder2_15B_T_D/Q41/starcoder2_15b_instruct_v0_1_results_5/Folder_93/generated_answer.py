def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must have the same size')
    results = set()
    for element in list1:
        if element in list2:
            index = list2.index(element)
            if 75 <= index <= 94:
                results.add(element)
    return results