def identical_elements(list1, list2):
    assert len(list1) == len(list2), 'The lists must be of the same size.'
    identical_elements_set = set()
    for elem1, elem2 in zip(list1, list2):
        if elem1 == elem2:
            identical_elements_set.add(elem1)
    return identical_elements_set