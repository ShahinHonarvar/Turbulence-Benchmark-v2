def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists are not the same size.')
    common_elements = set(list1[62:79]) & set(list2[62:79])
    return common_elements