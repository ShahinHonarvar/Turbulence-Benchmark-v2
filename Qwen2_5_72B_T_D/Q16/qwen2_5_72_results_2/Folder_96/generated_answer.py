def sum_even_ints_inclusive(numbers):
    return sum((number for number in numbers[50:201] if number % 2 == 0))