def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    elements = set()
    for i in range(len(list1)):
        if list1[i] == list2[i] and 310 <= i <= 370:
            elements.add(list1[i])
    return elements