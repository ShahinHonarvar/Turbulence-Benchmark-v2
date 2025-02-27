def identical_elements(list1, list2):
    num_elements = len(list1)
    common_elements = set()
    for index in range(num_elements):
        if index >= 5 and index <= 7:
            if list1[index] in list2:
                common_elements.add(list1[index])
    return common_elements