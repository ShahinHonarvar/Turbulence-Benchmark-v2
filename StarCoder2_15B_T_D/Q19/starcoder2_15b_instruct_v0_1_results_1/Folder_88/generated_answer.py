def all_ints_not_div_by_num(ints):
    result = []
    for i, num in enumerate(ints):
        if i >= 4 and i < 7 and (num % -6 != 0):
            result.append(num)
    return result