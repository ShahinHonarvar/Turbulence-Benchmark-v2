def identical_elements(list1, list2):
    result = set()
    for i in range(661, 925):
        if list1[i] == list2[i]:
            result.add(list1[i])
    return result