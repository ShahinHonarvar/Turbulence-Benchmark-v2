def all_ints_not_div_by_num(numbers):
    return [num for idx, num in enumerate(numbers) if idx >= 10 and idx < 100 and (num % 100 != 0)]