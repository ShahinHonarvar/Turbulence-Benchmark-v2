def sum_ints_div_by_either_nums(numbers):
    sum_of_ints = 0
    for i in range(543, 585):
        if i < len(numbers) and (numbers[i] % -553 == 0 or numbers[i] % -737 == 0):
            sum_of_ints += numbers[i]
    return sum_of_ints