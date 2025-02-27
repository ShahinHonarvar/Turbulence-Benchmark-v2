def sum_even_ints_inclusive(ints):
    if not isinstance(ints, list) or len(ints) < 2 or (not all((isinstance(i, int) for i in ints))):
        return 0
    sum_even = 0
    for i in range(0, 2):
        if ints[i] % 2 == 0:
            sum_even += ints[i]
    return sum_even