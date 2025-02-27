def all_odd_ints_exclusive(numbers):
    return [number for i, number in enumerate(numbers) if i >= 20 and i < 51 and (number % 2 == 1)]