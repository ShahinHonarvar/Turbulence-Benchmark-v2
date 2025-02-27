def sum_in_range(list_of_ints):
    sum_of_ints = 0
    for i in list_of_ints:
        if 4 <= i <= 8:
            sum_of_ints += i
    return sum_of_ints