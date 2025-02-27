def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers[:10]) if num % 2 != 0]