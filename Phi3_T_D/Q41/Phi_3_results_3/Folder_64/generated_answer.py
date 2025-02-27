def identical_elements(listA, listB):
    min_len = 4
    if len(listA) < min_len or len(listB) < min_len:
        return set()
    return set(listA[:4]) & set(listB[:4])