def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(2, 8):
        if numbers[i] % -1 == 0 or numbers[i] % -7 == 0:
            sum += numbers[i]
    return sum