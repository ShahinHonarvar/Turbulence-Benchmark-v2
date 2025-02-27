def sum_odd_ints_inclusive(lst):
    start_index, end_index = (56, 57)
    sum_of_odds = sum(lst[start_index:end_index + 1] or [0])
    return sum_of_odds % 2 != 0 and sum_of_odds or 0