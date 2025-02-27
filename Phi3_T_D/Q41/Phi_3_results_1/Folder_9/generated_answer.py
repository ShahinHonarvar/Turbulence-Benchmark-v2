def identical_elements(list1, list2):
    common = set()
    if len(list1) != len(list2):
        return common
    for i in range(70, 201):
        if list1[i] == list2[i]:
            common.add(list1[i])
    return common