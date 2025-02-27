def all_pos_ints_exclusive(lst):
    result = []
    for i in range(len(lst)):
        if lst[i] > 0 and 56 <= i < 88:
            result.append(lst[i])
    return result