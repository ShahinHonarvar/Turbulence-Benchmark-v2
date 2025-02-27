def all_ints_div_by_num(numbers):
    return [num for i, num in enumerate(numbers) if i >= 13 and i <= 68 and (num % 71 == 0)]