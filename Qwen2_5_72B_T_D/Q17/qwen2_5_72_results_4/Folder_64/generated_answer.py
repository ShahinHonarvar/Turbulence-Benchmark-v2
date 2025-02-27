def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in lst[:4]:
        if i % 11 == 0 and i % -7 == 0:
            result.append(i)
    return result