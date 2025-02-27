def identical_elements(list1, list2):
    result = set()
    for i in range(31, 73):
        if list1[i] in list2:
            result.add(list1[i])
    return result