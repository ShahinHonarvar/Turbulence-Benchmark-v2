def sum_ints_div_by_either_nums(numbers):
    sum_of_ints = 0
    for i in range(138, 425):
        if numbers[i] % -863 == 0 or numbers[i] % -329 == 0:
            sum_of_ints += numbers[i]
    return sum_of_ints