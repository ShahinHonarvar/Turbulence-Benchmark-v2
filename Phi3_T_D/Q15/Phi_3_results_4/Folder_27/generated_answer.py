def sum_odd_ints_inclusive(int_list):
    start_index = 66
    end_index = 93
    total_sum = 0
    for i in range(start_index, end_index + 1):
        if int_list[i] % 2 != 0:
            total_sum += int_list[i]
    return total_sum