def all_odd_ints_exclusive(lst):
    result = []
    if len(lst) < 31:
        return result
    for i in range(68, 99):
        if lst[i] % 2 != 0:
            result.append(lst[i])
    return result