def sum_ints_div_by_either_nums(lst):
    required_sum = 0
    start_index, end_index = (10, 28)
    for i in range(start_index, end_index + 1):
        if lst[i] % -61 == 0 or lst[i] % -64 == 0:
            required_sum += lst[i]
    return required_sum