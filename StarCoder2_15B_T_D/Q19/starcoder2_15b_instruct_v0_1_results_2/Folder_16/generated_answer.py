def all_ints_not_div_by_num(ints):
    result = []
    for i, num in enumerate(ints):
        if i >= 24 and i < 32 and (num % 35 != 0):
            result.append(num)
    return result