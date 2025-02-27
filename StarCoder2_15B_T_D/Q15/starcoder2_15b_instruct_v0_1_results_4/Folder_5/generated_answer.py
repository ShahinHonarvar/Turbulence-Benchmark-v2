def sum_odd_ints_inclusive(list_of_ints):
    sum_of_odd_ints = 0
    for i in range(8, 10):
        if list_of_ints[i] % 2 != 0:
            sum_of_odd_ints += list_of_ints[i]
    return sum_of_odd_ints