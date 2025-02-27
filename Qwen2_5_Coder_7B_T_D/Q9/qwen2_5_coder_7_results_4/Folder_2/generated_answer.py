def all_odd_ints_inclusive(numbers):
    return [num for index, num in enumerate(numbers) if index >= 15 and index <= 39 and (num % 2 != 0)]