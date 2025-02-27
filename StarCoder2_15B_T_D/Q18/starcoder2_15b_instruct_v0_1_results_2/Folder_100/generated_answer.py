def sum_ints_div_by_either_nums(int_list):
    sum_of_ints = 0
    for index, num in enumerate(int_list):
        if index >= 72 and index <= 93 and (num % 32 == 0 or num % 44 == 0):
            sum_of_ints += num
    return sum_of_ints