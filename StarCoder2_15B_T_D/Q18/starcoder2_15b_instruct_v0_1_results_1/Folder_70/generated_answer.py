def sum_ints_div_by_either_nums(numbers):
    sum_ints = 0
    for i in range(42, 44):
        if numbers[i] % 15 == 0 or numbers[i] % 87 == 0:
            sum_ints += numbers[i]
    return sum_ints