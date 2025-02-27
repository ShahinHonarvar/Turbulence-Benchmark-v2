def all_odd_ints_exclusive(numbers):
    return [num for index, num in enumerate(numbers) if index > 42 and index < 87 and (num % 2 != 0)]