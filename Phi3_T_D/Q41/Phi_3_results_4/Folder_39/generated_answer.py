def identical_elements(list1, list2):
    result_set = set()
    for i in range(20, 31):
        if i < len(list1) and i < len(list2):
            if list1[i] in list2:
                result_set.add(list1[i])
    return result_set