def all_odd_ints_inclusive(numbers):
    odd_ints = [num for i, num in enumerate(numbers) if i >= 62 and i <= 63 and (num % 2 != 0)]
    return odd_ints