def sum_ints_div_by_either_nums(numbers):
    sum_of_ints = 0
    for i in range(315, 935):
        if numbers[i] % -897 == 0 or numbers[i] % -556 == 0:
            sum_of_ints += numbers[i]
    return sum_of_ints