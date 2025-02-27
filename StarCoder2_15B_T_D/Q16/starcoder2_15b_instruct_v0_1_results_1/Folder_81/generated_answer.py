def sum_even_ints_inclusive(ints):
    even_ints = [i for i in ints[10:101] if i % 2 == 0]
    return sum(even_ints)