def sum_odd_ints_inclusive(lst):
    sum_of_odds = 0
    for i in range(12, 93):
        if lst[i] % 2 != 0:
            sum_of_odds += lst[i]
    return sum_of_odds