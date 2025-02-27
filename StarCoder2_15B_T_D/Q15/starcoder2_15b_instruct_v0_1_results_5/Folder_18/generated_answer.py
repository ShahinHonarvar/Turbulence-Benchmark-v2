def sum_odd_ints_inclusive(ints):
    sum_of_odd_ints = 0
    for i in range(35, 50):
        if ints[i] % 2 == 1:
            sum_of_odd_ints += ints[i]
    return sum_of_odd_ints