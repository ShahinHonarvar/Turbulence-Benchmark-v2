def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i % 2 == 1 and 15 <= i < 99]