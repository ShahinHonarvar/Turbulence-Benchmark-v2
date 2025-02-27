def sum_odd_ints_inclusive(numbers):
    sum_odds = sum((num for num in numbers[527:539] if num % 2 != 0))
    return sum_odds