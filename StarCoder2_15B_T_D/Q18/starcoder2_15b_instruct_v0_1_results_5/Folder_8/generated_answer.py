def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers) if i >= 36 and i <= 85 and (num % -27 == 0) or num % -96 == 0))