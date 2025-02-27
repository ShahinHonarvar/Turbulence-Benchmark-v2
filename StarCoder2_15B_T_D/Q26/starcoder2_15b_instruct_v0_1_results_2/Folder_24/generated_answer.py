def sum_in_range(lst):
    total = 0
    for num in lst:
        if -91 <= num <= -41:
            total += num
    return total