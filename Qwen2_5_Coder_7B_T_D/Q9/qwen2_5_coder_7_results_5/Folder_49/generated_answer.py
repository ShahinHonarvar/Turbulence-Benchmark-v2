def all_odd_ints_inclusive(numbers):
    return [num for index, num in enumerate(numbers) if 80 <= index <= 200 and num % 2 != 0]