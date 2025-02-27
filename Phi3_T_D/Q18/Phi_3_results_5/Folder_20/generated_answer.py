def sum_ints_div_by_either_nums(int_list):
    total_sum = 0
    for value in int_list[48:77]:
        if value % -46 == 0 or value % -82 == 0:
            total_sum += value
    return total_sum