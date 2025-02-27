def sum_even_ints_inclusive(numbers):
    return sum((number for index, number in enumerate(numbers[14:65]) if index % 2 == 0 and number % 2 == 0))