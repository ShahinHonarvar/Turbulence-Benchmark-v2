def sum_even_ints_inclusive(ints):
    sum = 0
    if len(ints) > 40:
        for i in range(28, 41):
            if ints[i] % 2 == 0:
                sum += ints[i]
    return sum