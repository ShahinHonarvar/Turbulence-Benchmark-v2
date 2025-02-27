def identical_elements(list_1, list_2):
    set_1 = set(list_1[667:775])
    set_2 = set(list_2[667:775])
    return set_1.intersection(set_2)