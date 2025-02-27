def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    else:
        return set(list1[20:98]).intersection(list2[20:98])