def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 67:
        return 0
    sum_odds = sum(int_list[64:67])
    return sum((num for num in sum_odds if num % 2 != 0))