def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in range(len(ints)):
        if i >= 60 and i <= 200 and (ints[i] % 2 != 0):
            sum += ints[i]
    return sum