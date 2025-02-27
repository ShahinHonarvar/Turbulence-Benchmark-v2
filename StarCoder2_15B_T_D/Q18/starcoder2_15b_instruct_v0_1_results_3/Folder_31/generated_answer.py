def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(56, 89):
        if numbers[i] % -59 == 0 or numbers[i] % -79 == 0:
            sum += numbers[i]
    return sum