def sum_ints_div_by_either_nums(numbers):
    divisible_sum = sum((num for num in numbers[315:935] if num % -897 == 0 or num % -556 == 0))
    return divisible_sum