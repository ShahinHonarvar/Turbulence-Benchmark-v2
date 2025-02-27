def sum_odd_ints_inclusive(numbers):
    return sum((x for i, x in enumerate(numbers[62:100]) if x % 2 != 0))