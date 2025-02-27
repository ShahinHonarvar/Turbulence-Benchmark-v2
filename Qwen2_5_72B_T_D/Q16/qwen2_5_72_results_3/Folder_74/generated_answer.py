def sum_even_ints_inclusive(numbers):
    return sum((numbers[i] for i in range(17, 79) if numbers[i] % 2 == 0))