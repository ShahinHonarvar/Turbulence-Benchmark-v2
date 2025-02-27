def all_ints_not_div_by_num(ints_list):
    result = []
    for i, num in enumerate(ints_list):
        if i >= 14 and i < 48 and (num % 16 != 0):
            result.append(num)
    return result