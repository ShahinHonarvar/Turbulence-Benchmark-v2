def identical_elements(list_1, list_2):
    assert len(list_1) == len(list_2), 'The two lists must be of the same size.'
    set_of_elements = set()
    for index in range(33, 37):
        element_1 = list_1[index]
        element_2 = list_2[index]
        if element_1 == element_2:
            set_of_elements.add(element_1)
    return set_of_elements