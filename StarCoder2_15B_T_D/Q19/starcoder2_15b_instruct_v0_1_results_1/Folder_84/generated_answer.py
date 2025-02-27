def all_ints_not_div_by_num(numbers):
    return [num for i, num in enumerate(numbers) if i >= 50 and i < 81 and (num % 64 != 0)]