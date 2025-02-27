def sum_ints_div_by_either_nums(numbers):
    sum_ints = 0
    for i in range(24, 33):
        if numbers[i] % 35 == 0 or numbers[i] % 87 == 0:
            sum_ints += numbers[i]
    return sum_ints