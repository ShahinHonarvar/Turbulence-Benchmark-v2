def sum_odd_ints_inclusive(ints):
    sum_ints = 0
    for i, num in enumerate(ints):
        if num % 2 == 1 and 29 <= i <= 51:
            sum_ints += num
    return sum_ints