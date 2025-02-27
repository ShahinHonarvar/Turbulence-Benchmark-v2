def all_ints_div_by_num(ints_list):
    result = []
    for i, num in enumerate(ints_list):
        if num % 5 == 0 and 0 <= i <= 5:
            result.append(num)
    return result