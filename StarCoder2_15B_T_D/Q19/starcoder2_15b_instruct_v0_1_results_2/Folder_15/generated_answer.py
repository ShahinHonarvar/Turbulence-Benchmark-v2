def all_ints_not_div_by_num(ints_list):
    result = []
    for i in range(len(ints_list)):
        if i >= 0 and i < 2:
            if ints_list[i] % -2 != 0:
                result.append(ints_list[i])
    return result