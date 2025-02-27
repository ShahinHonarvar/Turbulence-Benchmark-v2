def sum_ints_div_by_either_nums(numbers):
    sum_of_ints = 0
    for index in range(90, 98):
        num = numbers[index]
        if num % 13 == 0 or num % 35 == 0:
            sum_of_ints += num
    return sum_of_ints