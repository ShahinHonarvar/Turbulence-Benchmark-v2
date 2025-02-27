def all_odd_ints_exclusive(numbers):
    return [number for i, number in enumerate(numbers) if i >= 70 and i < 98 and (number % 2 == 1)]