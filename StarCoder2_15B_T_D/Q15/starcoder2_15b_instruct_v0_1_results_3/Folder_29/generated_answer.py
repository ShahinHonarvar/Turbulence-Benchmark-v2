def sum_odd_ints_inclusive(ints):
    sum_odd = 0
    for i in range(len(ints)):
        if i >= 59 and i <= 97 and (ints[i] % 2 == 1):
            sum_odd += ints[i]
    return sum_odd