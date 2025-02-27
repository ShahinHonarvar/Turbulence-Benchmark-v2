def sum_ints_div_by_either_nums(numbers):
    sum_divisible = 0
    for num in numbers:
        if num % -6 == 0 or num % 4 == 0:
            sum_divisible += num
    return sum_divisible