def identical_elements(list1, list2):
    return {x for x in set(list1) & set(list2) if list1.count(x) > 1 and list2.count(x) > 1}