def sum_ints_div_by_either_nums(numbers):
    total = sum(numbers[69:71])
    return sum((x for x in numbers[69:71] if x % 72 == 0 or x % 70 == 0)) or 0