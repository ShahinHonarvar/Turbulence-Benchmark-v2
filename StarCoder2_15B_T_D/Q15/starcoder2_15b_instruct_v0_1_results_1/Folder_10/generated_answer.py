def sum_odd_ints_inclusive(list_of_ints):
    sum_of_odds = 0
    for i in range(25, 60):
        if list_of_ints[i] % 2 != 0:
            sum_of_odds += list_of_ints[i]
    return sum_of_odds