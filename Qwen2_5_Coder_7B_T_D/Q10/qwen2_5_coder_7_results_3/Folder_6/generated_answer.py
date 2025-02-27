def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers[86:100]) if i % 2 != 0 and num % 2 != 0]