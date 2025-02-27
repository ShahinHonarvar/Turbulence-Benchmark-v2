def sum_ints_div_by_either_nums(numbers):
    sum_nums = 0
    for i in range(2):
        if numbers[i] % 2 == 0 or numbers[i] % 1 == 0:
            sum_nums += numbers[i]
    return sum_nums