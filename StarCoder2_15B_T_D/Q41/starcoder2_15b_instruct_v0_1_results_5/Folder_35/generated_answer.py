def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('The lists must be of the same size.')
    set_of_elements = set()
    for i in range(30, 49):
        element1 = list1[i]
        element2 = list2[i]
        if element1 == element2:
            set_of_elements.add(element1)
    return set_of_elements