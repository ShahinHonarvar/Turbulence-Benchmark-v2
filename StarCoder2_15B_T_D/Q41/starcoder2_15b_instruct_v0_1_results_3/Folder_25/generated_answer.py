def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    common_elements = set()
    for i in range(29, 94):
        if list1[i] == list2[i]:
            common_elements.add(list1[i])
    return common_elements