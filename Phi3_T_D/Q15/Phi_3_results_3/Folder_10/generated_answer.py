def sum_odd_ints_inclusive(numbers):
    start_index = 25
    end_index = 59
    sum_odds = sum((number for number in numbers[start_index:end_index + 1] if number % 2 != 0))
    return sum_odds