def identical_elements(list1, list2):
    common = set(list1).intersection(set(list2))
    return {x for x in common if list1.count(x) > 0 and list2.count(x) > 0 and (0 <= list1.index(x) <= 8) and (0 <= list2.index(x) <= 8)}