def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers) if i >= 77 and i <= 87 and (num % 23 == 0) or num % 57 == 0))