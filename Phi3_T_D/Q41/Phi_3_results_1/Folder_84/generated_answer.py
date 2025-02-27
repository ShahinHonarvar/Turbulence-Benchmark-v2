def identical_elements(list1, list2):
    common_elements = set()
    for i in range(43, 87):
        if i < len(list1) and i < len(list2):
            element1, element2 = (list1[i], list2[i])
            if element1 in list2[43:87 + 1] and element1 in list1[43:86 + 1]:
                common_elements.add(element1)
    return common_elements