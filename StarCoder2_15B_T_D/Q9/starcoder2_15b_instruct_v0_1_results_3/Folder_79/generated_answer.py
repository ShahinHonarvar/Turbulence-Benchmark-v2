def all_odd_ints_inclusive(numbers):
    return [number for index, number in enumerate(numbers) if index >= 4 and index <= 4 and (number % 2 == 1)]