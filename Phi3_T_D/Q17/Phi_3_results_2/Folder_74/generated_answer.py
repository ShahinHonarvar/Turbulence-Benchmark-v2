def all_ints_div_by_both_two_nums(numbers):
    if len(numbers) < 98:
        return []
    return [num for num in numbers[90:98] if num % 13 == 0 and num % 35 == 0]