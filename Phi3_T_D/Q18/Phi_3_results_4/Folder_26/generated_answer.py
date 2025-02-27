def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(69, 71):
        if numbers[i] % 72 == 0 or numbers[i] % 70 == 0:
            sum += numbers[i]
    return sum