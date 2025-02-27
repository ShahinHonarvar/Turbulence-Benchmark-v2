def sum_even_ints_inclusive(ints):
    total = 0
    for i in range(len(ints)):
        if 5 <= i <= 7 and ints[i] % 2 == 0:
            total += ints[i]
    return total