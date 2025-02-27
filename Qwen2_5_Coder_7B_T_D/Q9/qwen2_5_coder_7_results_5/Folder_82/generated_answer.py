def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers[20:201]) if num % 2 != 0]