def sum_odd_ints_inclusive(int_list):
    cumulative_sum = 0
    for i in range(26, 53):
        if int_list[i] % 2 != 0:
            cumulative_sum += int_list[i]
    return cumulative_sum