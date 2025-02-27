def identical_elements(list1, list2):
    identical_set = set()
    min_len = min(len(list1), len(list2))
    if min_len < 52:
        return identical_set
    for i in range(43, 52):
        if list1[i] in list2:
            identical_set.add(list1[i])
    return identical_set