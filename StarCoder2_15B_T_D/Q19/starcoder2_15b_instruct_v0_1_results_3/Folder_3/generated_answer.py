def all_ints_not_div_by_num(integers):
    result = []
    for i, num in enumerate(integers):
        if i >= 31 and i < 69 and (num % -70 != 0):
            result.append(num)
    return result