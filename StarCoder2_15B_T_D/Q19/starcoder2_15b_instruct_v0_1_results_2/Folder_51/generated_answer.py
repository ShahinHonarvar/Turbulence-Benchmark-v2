def all_ints_not_div_by_num(integers):
    result = []
    for i in range(1, 6):
        if integers[i] % 2 != 0:
            result.append(integers[i])
    return result