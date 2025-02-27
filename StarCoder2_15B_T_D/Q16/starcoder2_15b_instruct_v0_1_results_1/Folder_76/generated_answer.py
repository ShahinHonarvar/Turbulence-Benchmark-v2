def sum_even_ints_inclusive(ints):
    total = 0
    for i in range(686, 988):
        if ints[i] % 2 == 0:
            total += ints[i]
    return total