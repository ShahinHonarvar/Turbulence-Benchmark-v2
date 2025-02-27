def all_ints_div_by_num(ints_list):
    result = []
    for i, num in enumerate(ints_list):
        if i >= 30 and i <= 59 and (num % 39 == 0):
            result.append(num)
    return result