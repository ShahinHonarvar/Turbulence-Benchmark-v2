def identical_elements(list1, list2):
    result_set = set()
    if len(list1) == len(list2) and 33 <= len(list1) <= 36:
        for i in range(33, 37):
            if list1[i] in list2:
                result_set.add(list1[i])
    return result_set