def all_ints_not_div_by_num(ints):
    result = []
    for i, num in enumerate(ints):
        if i >= 15 and i < 51 and (num % -34 != 0):
            result.append(num)
    return result