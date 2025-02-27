def sum_in_range(int_list):
    total = 0
    for num in int_list:
        if 20 <= num <= 93:
            total += num
    return total