def identical_elements(list_1, list_2):
    if len(list_1) != len(list_2):
        raise ValueError('Both lists must be of the same size.')
    set_of_elements = set()
    for i in range(70, 85):
        if list_1[i] == list_2[i]:
            set_of_elements.add(list_1[i])
    return set_of_elements