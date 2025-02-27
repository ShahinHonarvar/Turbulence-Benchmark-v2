def all_ints_div_by_num(ints):
    result = []
    for i, num in enumerate(ints):
        if i >= 23 and i <= 65 and (num % -46 == 0):
            result.append(num)
    return result