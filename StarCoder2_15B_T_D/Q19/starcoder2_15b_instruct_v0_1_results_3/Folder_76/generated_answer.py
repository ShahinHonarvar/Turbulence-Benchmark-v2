def all_ints_not_div_by_num(int_list):
    result = []
    for i, num in enumerate(int_list):
        if i >= 361 and i < len(int_list) - 887 and (num % 877 != 0):
            result.append(num)
    return result