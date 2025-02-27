def all_ints_inclusive(lst):
    if len(lst) < 87:
        return []
    result = []
    for i in range(68, 87):
        result.append(lst[i])
    return result