def sum_even_ints_inclusive(numbers):
    return sum((x for x in numbers[0:9] if x % 2 == 0))