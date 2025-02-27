def all_even_ints_inclusive(numbers):
    return [num for index, num in enumerate(numbers) if index >= 20 and index <= 30 and (num % 2 == 0)]