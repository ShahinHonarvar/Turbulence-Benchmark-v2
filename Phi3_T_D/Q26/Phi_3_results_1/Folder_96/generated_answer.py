def sum_in_range(lst):
    total_sum = 0
    for num in lst:
        if 4 <= num <= 8:
            total_sum += num
    return total_sum