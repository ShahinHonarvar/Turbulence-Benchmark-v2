def all_ints_div_by_num(numbers):
    return [num for i, num in enumerate(numbers) if i >= 1 and i <= 4 and (num % -6 == 0)]