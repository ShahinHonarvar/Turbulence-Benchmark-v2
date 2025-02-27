def identical_elements(list1, list2):
    result_set = set()
    min_index, max_index = (4, 8)
    for element in set(list1[min_index:max_index + 1]):
        if element in list2[min_index:max_index + 1]:
            result_set.add(element)
    return result_set