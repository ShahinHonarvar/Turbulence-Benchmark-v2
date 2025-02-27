def sum_even_ints_inclusive(ints):
    sum_even_ints = 0
    for i in ints:
        if i % 2 == 0:
            sum_even_ints += i
    return sum_even_ints