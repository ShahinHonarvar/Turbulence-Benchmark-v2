def sum_ints_div_by_either_nums(int_list):
    total_sum = 0
    for number in int_list[22:25]:
        if number % -85 == 0 or number % -30 == 0:
            total_sum += number
    return total_sum