def all_ints_not_div_by_num(ints):
    result = []
    for i, num in enumerate(ints):
        if i >= 43 and i < 77 and (num % 84 != 0):
            result.append(num)
    return result