def all_ints_div_by_num(numbers):
    result = [num for i, num in enumerate(numbers) if 13 <= i <= 63 and num % 46 == 0]
    return result