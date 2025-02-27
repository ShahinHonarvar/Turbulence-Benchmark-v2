def sum_ints_div_by_either_nums(numbers):
    relevant_numbers = numbers[29:46]
    sum_numbers = sum((num for num in relevant_numbers if num % 27 == 0 or num % 81 == 0))
    return sum_numbers