def all_ints_not_div_by_num(ints):
    result = []
    for i, num in enumerate(ints):
        if i >= 38 and i < 52 and (num % -41 != 0):
            result.append(num)
    return result