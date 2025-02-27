def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers[1:8]) if i % 2 == 0 and num % 2 != 0]