def identical_elements(list1, list2):
    assert len(list1) == len(list2), 'The two lists must be of the same size.'
    common_elements = set()
    for i in range(13, 69):
        if list1[i] == list2[i]:
            common_elements.add(list1[i])
    return common_elements