def sum_even_ints_inclusive(ints):
    sum_even = 0
    for i in range(50, 55):
        if ints[i] % 2 == 0:
            sum_even += ints[i]
    return sum_even