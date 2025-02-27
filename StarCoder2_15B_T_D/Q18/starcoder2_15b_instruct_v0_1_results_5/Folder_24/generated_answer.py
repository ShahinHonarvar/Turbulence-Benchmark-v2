def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers) if i >= 29 and i <= 53 and (num % -68 == 0) or num % -85 == 0))