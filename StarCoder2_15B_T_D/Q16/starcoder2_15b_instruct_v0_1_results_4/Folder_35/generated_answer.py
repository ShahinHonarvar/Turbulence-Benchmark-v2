def sum_even_ints_inclusive(ints):
    sum_even_ints = 0
    for i in range(30, 49):
        if ints[i] % 2 == 0:
            sum_even_ints += ints[i]
    return sum_even_ints