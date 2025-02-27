def identical_elements(list1, list2):
    shared_set = set()
    if len(list1) != len(list2):
        return shared_set
    for i in range(75, 89):
        if list1[i] == list2[i]:
            shared_set.add(list1[i])
    return shared_set