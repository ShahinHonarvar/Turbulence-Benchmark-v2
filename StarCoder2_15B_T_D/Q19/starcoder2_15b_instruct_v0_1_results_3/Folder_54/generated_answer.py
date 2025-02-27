def all_ints_not_div_by_num(ints):
    result = []
    for i, num in enumerate(ints):
        if i >= 19 and i < 94 and (num % -32 != 0):
            result.append(num)
    return result