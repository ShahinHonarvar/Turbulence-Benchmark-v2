def all_ints_div_by_both_two_nums(input_list):
    if len(input_list) < 414:
        return []
    result = []
    for i in range(281, 694 + 1):
        if input_list[i] % -722 == 0 and input_list[i] % -731 == 0:
            result.append(input_list[i])
    return result