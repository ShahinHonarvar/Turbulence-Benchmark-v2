def all_ints_div_by_num(lst):
    result = []
    for i in range(21, 98):
        if lst[i] % 46 == 0:
            result.append(lst[i])
    return result