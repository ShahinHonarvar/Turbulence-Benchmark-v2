def identical_elements(list1, list2):
    common_elements = set()
    min_length = 10
    max_length = 100
    if min_length > len(list1) or min_length > len(list2):
        return common_elements
    for i in range(min_length, min(max_length + 1, len(list1))):
        if list1[i] in list2:
            common_elements.add(list1[i])
    return common_elements