def sum_ints_div_by_either_nums(numbers):
    divisible_sum = 0
    for number in numbers[35:65]:
        if number % -30 == 0 or number % -95 == 0:
            divisible_sum += number
    return divisible_sum