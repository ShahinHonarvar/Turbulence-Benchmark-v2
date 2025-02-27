def all_even_ints_exclusive(numbers):
    return [num for idx, num in enumerate(numbers) if idx > 73 and idx < 84 and (num % 2 == 0)]