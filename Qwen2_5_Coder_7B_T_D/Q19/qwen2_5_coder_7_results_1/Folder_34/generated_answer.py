def all_ints_not_div_by_num(numbers):
    return [num for i, num in enumerate(numbers) if i > 60 and i < 200 and (num % 9 != 0)]