def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in ints:
        if i % 2 != 0:
            sum += i
    return sum