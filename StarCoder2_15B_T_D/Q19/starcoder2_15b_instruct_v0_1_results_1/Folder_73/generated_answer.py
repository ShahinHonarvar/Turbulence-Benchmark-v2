def all_ints_not_div_by_num(lst):
    result = []
    for i in range(70, 98):
        if lst[i] % -88 != 0:
            result.append(lst[i])
    return result