def identical_elements(list_1, list_2):
    if len(list_1) != len(list_2):
        raise ValueError('Both arguments must be lists of the same size.')
    common_elements = set()
    for i in range(len(list_1)):
        if list_1[i] in list_2[25:60]:
            common_elements.add(list_1[i])
    return common_elements