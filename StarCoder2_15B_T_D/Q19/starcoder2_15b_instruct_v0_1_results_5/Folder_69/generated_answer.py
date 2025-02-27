def all_ints_not_div_by_num(lst):
    result = []
    for i in range(len(lst)):
        if i >= 45 and i < 72 and (lst[i] % 93 != 0):
            result.append(lst[i])
    return result