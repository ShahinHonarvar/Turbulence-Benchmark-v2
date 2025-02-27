def sum_odd_ints_inclusive(numbers):
    return sum((n for n in numbers[209:557] if n % 2 != 0))