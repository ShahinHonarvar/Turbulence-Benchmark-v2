def sum_odd_ints_inclusive(int_list):
    sum_odds = 0
    for i in range(36, 47):
        if int_list[i] % 2 != 0:
            sum_odds += int_list[i]
    return sum_odds