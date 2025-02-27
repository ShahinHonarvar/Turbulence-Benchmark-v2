def sum_ints_div_by_either_nums(int_list):
    total_sum = 0
    for num in int_list[80:90]:
        if num % 56 == 0 or num % 68 == 0:
            total_sum += num
    return total_sum