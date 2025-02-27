def sum_ints_div_by_either_nums(int_list):
    sum_div = 0
    for num in int_list[42:44]:
        if num % 15 == 0 or num % 87 == 0:
            sum_div += num
    return sum_div