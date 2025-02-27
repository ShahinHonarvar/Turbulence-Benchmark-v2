def all_odd_ints_exclusive(numbers):
    return [num for index, num in enumerate(numbers) if index > 0 and index < 5 and (num % 2 != 0)]