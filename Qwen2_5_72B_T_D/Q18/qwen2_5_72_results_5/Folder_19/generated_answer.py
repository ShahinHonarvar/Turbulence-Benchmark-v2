def sum_ints_div_by_either_nums(numbers):
    relevant_numbers = numbers[1:5]
    sum_divisible = sum((num for num in relevant_numbers if num % 4 == 0 or num % -6 == 0))
    return sum_divisible