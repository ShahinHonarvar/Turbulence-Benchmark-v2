def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in ints[4:5]:
        if i % 2 != 0:
            sum += i
    return sum