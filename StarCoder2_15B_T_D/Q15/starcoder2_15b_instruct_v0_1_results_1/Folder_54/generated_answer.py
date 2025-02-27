def sum_odd_ints_inclusive(ints):
    sum_odd = 0
    for i in ints:
        if i % 2 == 1:
            sum_odd += i
    return sum_odd