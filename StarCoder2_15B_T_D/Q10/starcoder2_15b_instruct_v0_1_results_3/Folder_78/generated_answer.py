def all_odd_ints_exclusive(numbers):
    return [number for index, number in enumerate(numbers) if index >= 20 and index < 35 and (number % 2 == 1)]