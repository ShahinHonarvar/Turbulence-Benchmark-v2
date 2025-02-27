def all_ints_div_by_num(ints_list):
    result = []
    for i in ints_list:
        if i % 1 == 0:
            result.append(i)
    return result