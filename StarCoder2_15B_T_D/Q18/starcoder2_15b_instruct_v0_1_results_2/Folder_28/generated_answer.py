def sum_ints_div_by_either_nums(ints_list):
    ints_div_by_either_nums = []
    for i in range(len(ints_list)):
        if i >= 34 and i <= 81 and (ints_list[i] % 27 == 0) or ints_list[i] % 57 == 0:
            ints_div_by_either_nums.append(ints_list[i])
    return sum(ints_div_by_either_nums)