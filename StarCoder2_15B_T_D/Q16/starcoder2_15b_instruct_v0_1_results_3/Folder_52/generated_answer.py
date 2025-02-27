def sum_even_ints_inclusive(ints):
    total = 0
    num_even_ints = 0
    for i in range(len(ints)):
        if ints[i] % 2 == 0:
            total += ints[i]
            num_even_ints += 1
        if i >= 28 and num_even_ints == 11:
            break
    return total