def identical_elements(list1, list2):
    result = set()
    for i in range(len(list1)):
        if i >= 75 and i <= 85 and (list1[i] in list2):
            result.add(list1[i])
    return result