def sum_even_ints_inclusive(numbers):
    relevant_numbers = numbers[29:52]
    even_numbers = [num for num in relevant_numbers if num % 2 == 0]
    return sum(even_numbers)