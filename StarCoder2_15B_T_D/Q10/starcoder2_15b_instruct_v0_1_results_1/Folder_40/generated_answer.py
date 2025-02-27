def all_odd_ints_exclusive(numbers):
    return [number for index, number in enumerate(numbers) if index % 2 == 1]