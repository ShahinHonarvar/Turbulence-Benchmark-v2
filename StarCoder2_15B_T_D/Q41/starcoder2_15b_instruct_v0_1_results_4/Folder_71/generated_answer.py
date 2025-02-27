def identical_elements(list1, list2):
    set_of_elements = set()
    for i in range(26, 53):
        if list1[i] == list2[i]:
            set_of_elements.add(list1[i])
    return set_of_elements