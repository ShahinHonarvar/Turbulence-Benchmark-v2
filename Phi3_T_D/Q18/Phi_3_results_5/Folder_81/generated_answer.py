def sum_ints_div_by_either_nums(numbers):
    sum_div = sum((n for n in numbers[10:101] if n % 10 == 0 or n % 100 == 0))
    return sum_div