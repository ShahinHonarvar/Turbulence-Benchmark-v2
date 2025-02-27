def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    set1 = set(list1[91:100])
    set2 = set(list2[91:100])
    return set1 & set2