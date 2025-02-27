def all_ints_div_by_num(int_list):
    result = []
    for i, num in enumerate(int_list):
        if i >= 42 and i <= 89 and (num % -59 == 0):
            result.append(num)
    return result