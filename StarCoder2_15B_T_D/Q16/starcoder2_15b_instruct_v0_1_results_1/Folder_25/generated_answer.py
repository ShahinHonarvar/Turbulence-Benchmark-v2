def sum_even_ints_inclusive(ints):
    if not isinstance(ints, list) or not all((isinstance(i, int) for i in ints)):
        raise TypeError('Argument must be a list of integers')
    sum_even = 0
    for i in range(29, 94):
        if ints[i] % 2 == 0:
            sum_even += ints[i]
    return sum_even