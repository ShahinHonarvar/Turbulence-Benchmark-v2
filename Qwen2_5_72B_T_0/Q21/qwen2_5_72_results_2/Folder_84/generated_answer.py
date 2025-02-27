def all_ints_div_by_num(lst):
    result = []
    for i in range(52, 54):
        if i < len(lst) and lst[i] % 93 == 0:
            result.append(lst[i])
    return result