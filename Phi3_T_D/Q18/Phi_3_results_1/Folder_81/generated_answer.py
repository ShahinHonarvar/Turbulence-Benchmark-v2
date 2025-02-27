def sum_ints_div_by_either_nums(numbers):
    return sum((x for x in numbers[10:101] if x % 10 == 0 or x % 100 == 0))