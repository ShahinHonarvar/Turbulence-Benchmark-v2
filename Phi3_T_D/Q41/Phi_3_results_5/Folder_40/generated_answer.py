def identical_elements(list1, list2):
    return {item for item in set(list1) & set(list2) if list1.count(item) > 0 and list2.count(item) > 0}