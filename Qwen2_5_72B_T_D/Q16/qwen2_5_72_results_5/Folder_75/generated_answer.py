def sum_even_ints_inclusive(numbers):
    slice_of_numbers = numbers[56:58]
    even_numbers = [num for num in slice_of_numbers if num % 2 == 0]
    return sum(even_numbers)