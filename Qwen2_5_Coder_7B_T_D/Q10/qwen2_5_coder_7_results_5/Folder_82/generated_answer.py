def all_odd_ints_exclusive(numbers):
    return [num for index, num in enumerate(numbers) if index > 20 and index < 200 and (num % 2 != 0)]