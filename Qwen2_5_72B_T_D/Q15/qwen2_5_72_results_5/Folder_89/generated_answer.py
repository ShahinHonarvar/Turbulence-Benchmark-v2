def sum_odd_ints_inclusive(numbers):
    relevant_numbers = numbers[56:83]
    odd_numbers = [num for num in relevant_numbers if num % 2 != 0]
    return sum(odd_numbers)