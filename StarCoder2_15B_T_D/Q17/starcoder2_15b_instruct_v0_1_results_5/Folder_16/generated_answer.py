def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(5, 81):
        if lst[i] % 44 == 0:
            result.append(lst[i])
    return result