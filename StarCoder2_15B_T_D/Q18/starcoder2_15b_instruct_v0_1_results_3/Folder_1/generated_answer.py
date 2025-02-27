def sum_ints_div_by_either_nums(int_list):
    total_sum = 0
    for i, num in enumerate(int_list):
        if i >= 10 and i <= 28 and (num % -61 == 0) or num % -64 == 0:
            total_sum += num
    return total_sum