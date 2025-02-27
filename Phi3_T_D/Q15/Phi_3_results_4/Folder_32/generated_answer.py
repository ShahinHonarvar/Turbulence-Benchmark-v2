def sum_odd_ints_inclusive(int_list):
    start_idx = 21
    end_idx = 97
    sum_odds = 0
    for i in range(start_idx, end_idx + 1):
        if int_list[i] % 2 != 0:
            sum_odds += int_list[i]
    return sum_odds