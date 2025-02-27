def sum_ints_div_by_either_nums(integers_list):
    sum = 0
    for i in range(46, 92):
        if integers_list[i] % 67 == 0 or integers_list[i] % 15 == 0:
            sum += integers_list[i]
    return sum