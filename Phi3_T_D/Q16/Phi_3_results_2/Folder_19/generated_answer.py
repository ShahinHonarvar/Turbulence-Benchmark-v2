def sum_even_ints_inclusive(numbers):
    even_sum = sum((num for idx, num in enumerate(numbers[2:6]) if num % 2 == 0))
    return even_sum