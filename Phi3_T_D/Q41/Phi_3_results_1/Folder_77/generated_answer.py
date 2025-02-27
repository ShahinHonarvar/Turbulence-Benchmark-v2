def identical_elements(list1, list2):
    if len(list1) < 538 or len(list2) < 538:
        return set()
    result_set = set()
    for index in range(527, 539):
        if list1[index] in list2:
            result_set.add(list1[index])
    return result_set