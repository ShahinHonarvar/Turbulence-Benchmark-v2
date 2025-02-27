def all_ints_not_div_by_num(lst):
    result = []
    for i in range(387, 516):
        if lst[i] % 310 != 0:
            result.append(lst[i])
    return result