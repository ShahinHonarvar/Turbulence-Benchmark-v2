def all_ints_not_div_by_num(input_list):
    result = []
    for i, num in enumerate(input_list):
        if i >= 8 and i < 9 and (num % 8 != 0):
            result.append(num)
    return result