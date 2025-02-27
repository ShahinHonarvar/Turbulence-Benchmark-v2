def sum_even_ints_inclusive(ints):
    total = 0
    for i in ints:
        if i % 2 == 0:
            total += i
    return total