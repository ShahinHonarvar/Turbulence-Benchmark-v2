def all_odd_ints_inclusive(int_list):
    all_odds = []
    for i, num in enumerate(int_list):
        if i >= 25 and i <= 87 and (num % 2 == 1):
            all_odds.append(num)
    return all_odds