def all_ints_div_by_num(ints_list):
    result = []
    for i in range(30, 301):
        if ints_list[i] % 5 == 0:
            result.append(ints_list[i])
    return result