def sum_odd_ints_inclusive(int_list):
    sum_odds = sum((x for x in int_list[40:42] if x % 2 != 0))
    return sum_odds