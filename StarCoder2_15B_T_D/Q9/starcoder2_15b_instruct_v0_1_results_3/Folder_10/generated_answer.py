def all_odd_ints_inclusive(numbers):
    return [n for n in numbers[25:60] if n % 2 == 1] if any((n % 2 == 1 for n in numbers[25:60])) else []