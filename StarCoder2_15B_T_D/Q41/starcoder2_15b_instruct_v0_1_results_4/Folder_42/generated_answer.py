def identical_elements(list1, list2):
    result = set()
    for i in range(len(list1)):
        if list1[i] == list2[i] and 29 <= i <= 79:
            result.add(list1[i])
    return result