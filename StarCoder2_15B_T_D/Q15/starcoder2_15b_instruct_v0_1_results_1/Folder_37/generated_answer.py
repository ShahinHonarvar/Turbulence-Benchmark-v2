def sum_odd_ints_inclusive(ints_list):
    sum_ints = 0
    for i in range(1, 6):
        if ints_list[i] % 2 != 0:
            sum_ints += ints_list[i]
    return sum_ints