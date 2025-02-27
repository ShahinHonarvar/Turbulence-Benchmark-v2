def all_ints_div_by_num(ints_list):
    result = []
    for i in range(255, 619):
        if ints_list[i] % 965 == 0:
            result.append(ints_list[i])
    return result