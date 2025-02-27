def sum_even_ints_inclusive(ints):
    even_ints = [i for i in ints[74:96] if i % 2 == 0]
    return sum(even_ints) if even_ints else 0