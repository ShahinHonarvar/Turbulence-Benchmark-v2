def identical_elements(list_1, list_2):
    if len(list_1) != len(list_2):
        raise ValueError('The lists must be of the same size.')
    return set(list_1[60:201]) & set(list_2[60:201])