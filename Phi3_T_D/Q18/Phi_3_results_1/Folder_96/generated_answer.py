def sum_ints_div_by_either_nums(numbers):
    s = 0
    for i in range(50, 201):
        if numbers[i] % -34 == 0 or numbers[i] % 64 == 0:
            s += numbers[i]
    return s