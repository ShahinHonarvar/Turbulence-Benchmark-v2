def all_odd_ints_inclusive(numbers):
    result = [n for i, n in enumerate(numbers[62:64], start=62) if n % 2 != 0]
    return result