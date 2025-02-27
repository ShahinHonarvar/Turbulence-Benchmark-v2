def all_pos_ints_inclusive(integers):
    result = []
    for i in range(40, 81):
        if integers[i] > 0:
            result.append(integers[i])
    return result