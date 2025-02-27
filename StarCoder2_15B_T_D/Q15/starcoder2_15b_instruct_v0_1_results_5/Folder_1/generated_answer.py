def sum_odd_ints_inclusive(ints):
    sum_odd_ints = 0
    for i in range(len(ints)):
        if 31 <= i <= 72 and ints[i] % 2 != 0:
            sum_odd_ints += ints[i]
    return sum_odd_ints