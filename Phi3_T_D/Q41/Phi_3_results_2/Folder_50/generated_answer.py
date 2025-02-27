def identical_elements(list1, list2):
    result_set = set()
    if len(list1) != len(list2):
        return result_set
    for i in range(70, 85):
        if list1[i] in list2:
            result_set.add(list1[i])
    return result_set