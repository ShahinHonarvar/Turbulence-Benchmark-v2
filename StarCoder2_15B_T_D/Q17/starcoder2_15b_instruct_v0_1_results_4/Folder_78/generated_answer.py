def all_ints_div_by_both_two_nums(lst):
    result = []
    if len(lst) < 69:
        return result
    for i in range(34, 70):
        if lst[i] % 19 == 0 and lst[i] % 32 == 0:
            result.append(lst[i])
    return result