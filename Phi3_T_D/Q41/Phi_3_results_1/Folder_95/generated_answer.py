def identical_elements(list1, list2):
    common_elements = set(list1[82:86] + list2[82:86])
    return {x for x in common_elements if list1.count(x) > 0 and list2.count(x) > 0}