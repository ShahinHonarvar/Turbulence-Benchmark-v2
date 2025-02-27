def identical_elements(list1, list2):
    common_elements = set()
    size = min(len(list1), len(list2))
    for i in range(6, min(8 + 1, size)):
        if list1[i] in list2:
            common_elements.add(list1[i])
    return common_elements