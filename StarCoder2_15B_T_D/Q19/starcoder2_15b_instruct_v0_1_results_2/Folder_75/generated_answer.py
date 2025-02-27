def all_ints_not_div_by_num(lst):
    result = []
    for i, num in enumerate(lst):
        if i >= 20 and i < 51 and (num % -48 != 0):
            result.append(num)
    return result