def sum_ints_div_by_either_nums(numbers):
    sum_of_ints = 0
    for i in range(90, 201):
        if numbers[i] % -31 == 0 or numbers[i] % 13 == 0:
            sum_of_ints += numbers[i]
    return sum_of_ints