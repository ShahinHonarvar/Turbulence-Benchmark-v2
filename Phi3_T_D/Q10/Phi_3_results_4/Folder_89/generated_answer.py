def all_odd_ints_exclusive(numbers):
    odd_ints = [n for i, n in enumerate(numbers[51:76]) if n % 2 != 0]
    return odd_ints