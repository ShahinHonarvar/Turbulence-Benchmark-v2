def sum_odd_ints_inclusive(numbers):
    return sum((x for i, x in enumerate(numbers[75:86]) if x % 2 != 0))