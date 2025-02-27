def sum_odd_ints_inclusive(ints):
    sum_ = 0
    for i in range(9):
        if ints[i] % 2 == 1:
            sum_ += ints[i]
    return sum_