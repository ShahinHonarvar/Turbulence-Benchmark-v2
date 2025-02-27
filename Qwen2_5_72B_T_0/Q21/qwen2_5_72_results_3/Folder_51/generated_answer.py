def all_ints_div_by_num(lst):
    result = []
    for i in range(5, 7):
        if i < len(lst) and lst[i] % -6 == 0:
            result.append(lst[i])
    return result