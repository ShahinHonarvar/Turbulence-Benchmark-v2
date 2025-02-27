def sum_even_ints_inclusive(numbers):
    return sum(numbers[30:201:2] if len(numbers) > 200 else [num for num in numbers[30:201] if num % 2 == 0])