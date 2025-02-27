def sum_odd_ints_inclusive(numbers):
    relevant_numbers = numbers[64:67]
    return sum((num for num in relevant_numbers if num % 2 != 0))