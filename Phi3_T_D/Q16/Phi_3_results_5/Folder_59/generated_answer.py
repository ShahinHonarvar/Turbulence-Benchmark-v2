def sum_even_ints_inclusive(integers):
    return sum((i for i in integers[:10] if i % 2 == 0))