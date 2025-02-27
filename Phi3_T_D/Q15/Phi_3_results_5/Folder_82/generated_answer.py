def sum_odd_ints_inclusive(integers):
    return sum((n for n in integers[20:201] if n % 2 != 0))