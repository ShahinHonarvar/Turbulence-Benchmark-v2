def sum_even_ints_inclusive(numbers):
    return sum((val for idx, val in enumerate(numbers) if idx >= 14 and idx <= 64 and (val % 2 == 0)))