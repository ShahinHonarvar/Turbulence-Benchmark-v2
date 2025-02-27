def identical_elements(list1, list2):
    common_elements = set()
    for item in list1[667:775]:
        if item in list2[667:775]:
            common_elements.add(item)
    return common_elements