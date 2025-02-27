def all_odd_ints_inclusive(numbers):
    return [num for index, num in enumerate(numbers) if index >= 19 and index <= 92 and (num % 2 != 0)]