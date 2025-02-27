def sum_even_ints_inclusive(numbers):
    return sum((numbers[i] for i in range(7) if i < len(numbers) and numbers[i] % 2 == 0))