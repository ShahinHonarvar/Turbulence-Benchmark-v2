def sum_odd_ints_inclusive(numbers):
    relevant_numbers = numbers[31:35]
    return sum((num for num in relevant_numbers if num % 2 != 0))