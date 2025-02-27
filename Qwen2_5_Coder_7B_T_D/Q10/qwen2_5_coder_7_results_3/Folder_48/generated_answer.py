def all_odd_ints_exclusive(numbers):
    return [num for index, num in enumerate(numbers) if index > 385 and index < 999 and (num % 2 != 0)]