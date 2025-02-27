def sum_odd_ints_inclusive(ints):
    total = 0
    for i, n in enumerate(ints):
        if 300 <= i <= 300 and n % 2 == 1:
            total += n
    return total