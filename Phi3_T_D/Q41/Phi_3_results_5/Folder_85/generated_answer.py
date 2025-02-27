def identical_elements(list1, list2):
    elements_common = {items for items in list1[6:9] if items in list2[6:9]}
    return elements_common