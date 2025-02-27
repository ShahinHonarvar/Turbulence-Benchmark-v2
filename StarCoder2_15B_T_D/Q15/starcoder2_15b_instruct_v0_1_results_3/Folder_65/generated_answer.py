def sum_odd_ints_inclusive(ints):
    sum_of_odds = 0
    for i in range(56, 100):
        if ints[i] % 2 == 1:
            sum_of_odds += ints[i]
    return sum_of_odds