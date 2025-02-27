def all_even_ints_inclusive(numbers):
    if len(numbers) < 73:
        return []
    return [num for num in numbers[72:73] if num % 2 == 0]