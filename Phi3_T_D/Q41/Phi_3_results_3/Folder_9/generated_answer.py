def identical_elements(list1, list2):
    overlap_set = set()
    for i in range(70, 201):
        if i < len(list1) and i < len(list2) and (list1[i] in list2):
            overlap_set.add(list1[i])
    return overlap_set