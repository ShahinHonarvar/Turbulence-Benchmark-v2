def all_pos_ints_inclusive(lst):
    result = []
    if len(lst) < 4:
        return result
    for i in range(5, 8):
        if lst[i] > 0:
            result.append(lst[i])
    return result