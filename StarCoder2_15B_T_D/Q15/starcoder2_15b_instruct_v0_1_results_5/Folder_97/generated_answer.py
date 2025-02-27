def sum_odd_ints_inclusive(integers):
    sum_of_odd_ints = 0
    for i in range(40, 81):
        if integers[i] % 2 == 1:
            sum_of_odd_ints += integers[i]
    return sum_of_odd_ints