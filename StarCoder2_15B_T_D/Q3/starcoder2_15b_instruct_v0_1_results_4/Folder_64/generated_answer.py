def all_pos_ints_inclusive(lst):
    result = []
    for i in range(len(lst)):
        if lst[i] > 0:
            result.append(lst[i])
        if i == 4:
            break
    return result