def all_ints_div_by_num(numbers):
    return [num for i, num in enumerate(numbers) if i >= 14 and i <= 56 and (num % -59 == 0)]