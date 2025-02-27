def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must be of the same size.')
    common_elements = {item for i in range(17, min(79, len(list1))) for item in (list1[i],) & set(list2)}
    return common_elements