def sum_ints_div_by_either_nums(numbers):
    div_sum = sum((num for num in numbers[56:89] if num % -59 == 0 or num % -79 == 0))
    return div_sum