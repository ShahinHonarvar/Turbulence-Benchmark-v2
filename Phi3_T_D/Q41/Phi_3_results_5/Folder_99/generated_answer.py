def identical_elements(list1, list2):
    assert len(list1) == len(list2)
    return set(list1[309:370]) & set(list2[309:370])