def all_ints_div_by_num(numbers):
    return [num for i, num in enumerate(numbers) if i >= 25 and i <= 41 and (num % -97 == 0)]