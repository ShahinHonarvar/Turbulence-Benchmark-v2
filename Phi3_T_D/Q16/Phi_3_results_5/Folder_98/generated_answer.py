def sum_even_ints_inclusive(integers):
    return sum((x for x in integers[:7] if x % 2 == 0))