def sum_even_ints_inclusive(ints):
    if len(ints) > 6:
        sum = 0
        for i in range(6, 7):
            if ints[i] % 2 == 0:
                sum += ints[i]
        return sum
    else:
        return 0