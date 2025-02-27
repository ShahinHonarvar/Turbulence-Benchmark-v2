def all_ints_div_by_num(ints_list):
    result = []
    for i in range(87, 90):
        if ints_list[i] % 55 == 0:
            result.append(ints_list[i])
    return result