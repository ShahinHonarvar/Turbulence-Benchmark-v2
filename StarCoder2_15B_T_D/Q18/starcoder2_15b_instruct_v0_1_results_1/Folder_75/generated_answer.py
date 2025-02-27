def sum_ints_div_by_either_nums(ints_list):
    sum_of_ints = 0
    for i in range(20, 94):
        if ints_list[i] % -92 == 0 or ints_list[i] % -50 == 0:
            sum_of_ints += ints_list[i]
    return sum_of_ints