def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in ints[33:37]:
        if i % 2 == 1:
            sum += i
    return sum