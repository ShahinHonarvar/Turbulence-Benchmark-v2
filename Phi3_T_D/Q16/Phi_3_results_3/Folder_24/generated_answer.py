def sum_even_ints_inclusive(numbers):
    total = sum((n for n in numbers[74:96] if n % 2 == 0))
    return total