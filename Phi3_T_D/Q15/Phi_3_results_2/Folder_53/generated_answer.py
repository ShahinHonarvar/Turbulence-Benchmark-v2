def sum_odd_ints_inclusive(int_list):
    sum_odds = sum((val for val in int_list[300:301] if val % 2 != 0))
    return sum_odds