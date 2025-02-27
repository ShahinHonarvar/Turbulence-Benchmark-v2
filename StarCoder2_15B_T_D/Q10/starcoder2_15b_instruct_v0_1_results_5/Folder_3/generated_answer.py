def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i in range(78, 93) and num % 2 == 1]