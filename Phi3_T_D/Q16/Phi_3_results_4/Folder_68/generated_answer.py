def sum_even_ints_inclusive(numbers):
    sum_even = sum((number for number in numbers[:9] if number % 2 == 0))
    return sum_even