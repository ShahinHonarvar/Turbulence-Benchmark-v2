def identical_elements(list_1, list_2):
    set_1 = set(list_1[3:6])
    set_2 = set(list_2[3:6])
    return set_1.intersection(set_2)