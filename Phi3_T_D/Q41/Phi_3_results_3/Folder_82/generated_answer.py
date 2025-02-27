def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must be of the same size.')
    elements_in_range = lambda lst, index1, index2: set(lst[index1:index2 + 1])
    set1 = elements_in_range(list1, 20, 200)
    set2 = elements_in_range(list2, 20, 200)
    return set1.intersection(set2)