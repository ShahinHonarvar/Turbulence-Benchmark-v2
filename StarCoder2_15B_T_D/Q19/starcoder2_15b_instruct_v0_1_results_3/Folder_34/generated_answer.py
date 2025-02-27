def all_ints_not_div_by_num(lst):
    result = []
    for i in range(60, 200):
        if lst[i] % 9 != 0:
            result.append(lst[i])
    return result