def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    relevant_elements_set = {list1[i] for i in range(82, 87) if i < len(list1) and i < len(list2) and (list1[i] in list2[i])}
    return relevant_elements_set