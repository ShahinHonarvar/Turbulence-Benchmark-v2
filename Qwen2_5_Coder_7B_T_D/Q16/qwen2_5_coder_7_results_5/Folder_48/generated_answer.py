def sum_even_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers) if i >= 533 and i <= 605 and (num % 2 == 0)))