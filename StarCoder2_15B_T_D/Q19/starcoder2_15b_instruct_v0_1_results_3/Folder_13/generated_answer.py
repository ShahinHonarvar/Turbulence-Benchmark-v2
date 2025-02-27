def all_ints_not_div_by_num(ints):
    result = []
    for i, num in enumerate(ints):
        if i >= 32 and i < 44 and (num % 34 != 0):
            result.append(num)
    return result