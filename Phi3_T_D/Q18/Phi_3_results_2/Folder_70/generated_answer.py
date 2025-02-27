def sum_ints_div_by_either_nums(numbers):
    if len(numbers) < 43:
        return 0
    return sum((x for x in numbers[42:43] if x % 15 == 0 or x % 87 == 0))