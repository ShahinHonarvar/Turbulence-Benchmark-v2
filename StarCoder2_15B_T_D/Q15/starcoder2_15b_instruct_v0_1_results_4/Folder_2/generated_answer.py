def sum_odd_ints_inclusive(ints):
    sum_odd_ints = 0
    for i, num in enumerate(ints):
        if i >= 15 and i <= 39 and (num % 2 != 0):
            sum_odd_ints += num
    return sum_odd_ints