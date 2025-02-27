def sum_odd_ints_inclusive(ints):
    sum_odd = 0
    for i in range(75, 89):
        if ints[i] % 2 == 1:
            sum_odd += ints[i]
    return sum_odd