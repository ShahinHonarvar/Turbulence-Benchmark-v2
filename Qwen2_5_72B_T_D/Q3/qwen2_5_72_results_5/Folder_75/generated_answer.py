def all_pos_ints_inclusive(lst):
    result = []
    for i in range(56, 58):
        if 0 < lst[i]:
            result.append(lst[i])
    return result