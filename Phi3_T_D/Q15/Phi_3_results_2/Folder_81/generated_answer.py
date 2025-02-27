def sum_odd_ints_inclusive(numbers):
    return sum((n for n in numbers[10:101] if n % 2 != 0))