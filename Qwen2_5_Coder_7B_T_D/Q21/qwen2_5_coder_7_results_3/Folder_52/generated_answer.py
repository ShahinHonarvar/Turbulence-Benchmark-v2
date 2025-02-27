def all_ints_div_by_num(numbers):
    return [num for i, num in enumerate(numbers) if i >= 42 and i <= 97 and (num % 46 == 0)]