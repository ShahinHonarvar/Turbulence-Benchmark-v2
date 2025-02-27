def all_ints_div_by_num(ints_list):
    result = []
    for i in range(22, 64):
        if ints_list[i] % -61 == 0:
            result.append(ints_list[i])
    return result