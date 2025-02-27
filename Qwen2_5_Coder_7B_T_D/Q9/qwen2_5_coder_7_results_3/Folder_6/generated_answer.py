def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers[10:67]) if i % 2 == 0 and num % 2 != 0]