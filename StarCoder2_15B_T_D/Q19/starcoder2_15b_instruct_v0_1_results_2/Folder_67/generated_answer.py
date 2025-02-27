def all_ints_not_div_by_num(lst):
    result = []
    for i in range(48, 92):
        if lst[i] % 90 != 0:
            result.append(lst[i])
    return result