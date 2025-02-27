def all_pos_ints_exclusive(integers):
    result = []
    for i in range(len(integers)):
        if 0 < integers[i] < 10:
            result.append(integers[i])
    return result