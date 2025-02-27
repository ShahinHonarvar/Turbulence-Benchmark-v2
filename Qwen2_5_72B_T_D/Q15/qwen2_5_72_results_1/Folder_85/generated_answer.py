def sum_odd_ints_inclusive(numbers):
    relevant_numbers = numbers[6:9]
    return sum((n for n in relevant_numbers if n % 2 != 0))