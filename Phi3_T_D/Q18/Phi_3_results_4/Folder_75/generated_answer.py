def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[20:94]) if num % -92 == 0 or num % -50 == 0))