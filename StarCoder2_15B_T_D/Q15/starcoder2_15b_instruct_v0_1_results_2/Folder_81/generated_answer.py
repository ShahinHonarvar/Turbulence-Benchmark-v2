def sum_odd_ints_inclusive(ints):
    sum = 0
    for i, num in enumerate(ints):
        if 10 <= i <= 100 and num % 2 != 0:
            sum += num
    return sum