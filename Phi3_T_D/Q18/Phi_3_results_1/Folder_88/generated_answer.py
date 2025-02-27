def sum_ints_div_by_either_nums(ints):
    start_index = 3
    end_index = 9
    total = 0
    for i in range(start_index, end_index + 1):
        if ints[i] % 6 == 0 or ints[i] % 1 == 0:
            total += ints[i]
    return total