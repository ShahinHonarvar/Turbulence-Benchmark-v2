def sum_odd_ints_inclusive(sequence):
    return sum((n for n in sequence[56:82:1] if n % 2 != 0))