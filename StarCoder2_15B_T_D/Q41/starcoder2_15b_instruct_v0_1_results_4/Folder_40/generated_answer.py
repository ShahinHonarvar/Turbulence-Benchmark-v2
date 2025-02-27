def identical_elements(list1, list2):
    result = set()
    for i in range(len(list1)):
        if list1[i] in list2[i:i + 2]:
            result.add(list1[i])
    return result