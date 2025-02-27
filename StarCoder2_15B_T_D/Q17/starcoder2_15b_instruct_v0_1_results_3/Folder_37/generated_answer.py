def all_ints_div_by_both_two_nums(numbers):
    return [num for i, num in enumerate(numbers) if i >= 2 and i <= 7 and (num % -1 == 0) and (num % -7 == 0)]