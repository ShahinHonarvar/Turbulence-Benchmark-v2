def all_ints_div_by_num(lst):
    result = []
    for i in range(12, 78):
        if lst[i] % -19 == 0:
            result.append(lst[i])
    return result