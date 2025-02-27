def identical_elements(list1, list2):
    if len(list1) == len(list2):
        result = set()
        for i in range(1, 6):
            if list1[i] in list2:
                result.add(list1[i])
        return result
    else:
        return set()