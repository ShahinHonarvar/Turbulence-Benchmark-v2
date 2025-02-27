def sum_ints_div_by_either_nums(numbers):
    sum_numbers = 0
    for number in numbers[24:33]:
        if number % 35 == 0 or number % 87 == 0:
            sum_numbers += number
    return sum_numbers