def identical_elements(list1, list2):
    if not list1 or not list2 or len(list1) != len(list2):
        return set()
    return {list1[i] for i in range(31, 35) if i < len(list1) and i < len(list2) and (list1[i] in list2[i])}