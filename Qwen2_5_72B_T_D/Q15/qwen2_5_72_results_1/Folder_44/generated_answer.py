def sum_odd_ints_inclusive(numbers):
    relevant_numbers = numbers[13:69]
    odd_integers_sum = sum((number for number in relevant_numbers if number % 2 != 0))
    return odd_integers_sum