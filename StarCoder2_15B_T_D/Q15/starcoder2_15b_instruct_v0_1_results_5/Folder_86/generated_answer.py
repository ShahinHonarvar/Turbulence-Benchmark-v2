def sum_odd_ints_inclusive(integers):
    sum = 0
    for i in range(31, 35):
        if integers[i] % 2 != 0:
            sum += integers[i]
    return sum