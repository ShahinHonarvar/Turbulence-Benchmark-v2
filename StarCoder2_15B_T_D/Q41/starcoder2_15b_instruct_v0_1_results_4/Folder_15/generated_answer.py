def identical_elements(list1, list2):
    if len(list1) == 0 or len(list2) == 0 or len(list1) != len(list2):
        return set()
    common_elements = set()
    for i in range(len(list1)):
        if list1[i] == list2[i] and 2 <= i <= 2:
            common_elements.add(list1[i])
    return common_elements