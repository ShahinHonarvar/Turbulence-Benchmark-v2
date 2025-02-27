def sum_even_ints_inclusive(numbers):
    even_sum = sum((number for number in numbers[:7] if number % 2 == 0))
    return even_sum