def sum_in_range(lst):
    total = 0
    for num in lst:
        if 2 <= num <= 9:
            total += num
    return total