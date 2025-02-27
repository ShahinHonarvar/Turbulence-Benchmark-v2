def sum_odd_ints_inclusive(int_list):
    sum_of_odds = 0
    for i, num in enumerate(int_list):
        if i >= 30 and i <= 87 and (num % 2 != 0):
            sum_of_odds += num
    return sum_of_odds