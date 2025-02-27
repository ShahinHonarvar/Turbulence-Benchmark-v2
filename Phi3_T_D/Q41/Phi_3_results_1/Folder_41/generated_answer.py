def identical_elements(list1, list2):
    common_elements = set(list1[6:7]) if len(list1) > 7 else set()
    for element in list2[6:7]:
        if element in list1[6:7]:
            common_elements.add(element)
    return common_elements