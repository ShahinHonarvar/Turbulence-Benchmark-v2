def all_ints_not_div_by_num(lst):
    result = []
    for i, num in enumerate(lst):
        if i >= 84 and i < 86 and (num % 99 != 0):
            result.append(num)
    return result