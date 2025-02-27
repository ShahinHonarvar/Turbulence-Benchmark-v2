def all_ints_not_div_by_num(lst):
    result = []
    for i, num in enumerate(lst):
        if i >= 21 and i < 51 and (num % -77 != 0):
            result.append(num)
    return result