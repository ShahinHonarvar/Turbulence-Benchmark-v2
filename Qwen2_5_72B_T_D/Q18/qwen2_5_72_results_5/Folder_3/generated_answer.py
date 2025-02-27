def sum_ints_div_by_either_nums(numbers):
    relevant_numbers = numbers[38:53]
    return sum((num for num in relevant_numbers if num % -41 == 0 or num % -47 == 0))