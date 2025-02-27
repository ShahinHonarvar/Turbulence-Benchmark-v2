def all_ints_div_by_num(lst):
    result = []
    if len(lst) >= 353:
        for i in range(315, 353):
            if lst[i] % -858 == 0:
                result.append(lst[i])
    return result