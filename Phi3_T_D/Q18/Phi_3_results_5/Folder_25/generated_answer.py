def sum_ints_div_by_either_nums(numbers):
    return sum((x for x in numbers[25:81] if x % -20 == 0 or x % -26 == 0))