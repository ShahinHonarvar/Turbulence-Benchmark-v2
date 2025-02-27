def sum_odd_ints_inclusive(numbers):
    sum_of_odds = 0
    for i in range(50, 201):
        if numbers[i] % 2 == 1:
            sum_of_odds += numbers[i]
    return sum_of_odds