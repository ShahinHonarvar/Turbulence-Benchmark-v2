def all_ints_not_div_by_num(lst):
    result = []
    for i, num in enumerate(lst):
        if i >= 24 and i < 25 and (num % -30 != 0):
            result.append(num)
    return result