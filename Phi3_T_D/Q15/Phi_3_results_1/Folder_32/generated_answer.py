def sum_odd_ints_inclusive(numbers):
    return sum((n for n in numbers[20:98] if n % 2 != 0))