def sum_ints_div_by_either_nums(integers):
    sum = 0
    for i in range(28, 97):
        if integers[i] % 90 == 0 or integers[i] % 97 == 0:
            sum += integers[i]
    return sum