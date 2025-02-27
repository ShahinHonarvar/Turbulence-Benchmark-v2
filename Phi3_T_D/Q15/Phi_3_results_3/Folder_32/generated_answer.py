def sum_odd_ints_inclusive(numbers):
    total_sum = sum((num for num in numbers[20:98] if num % 2 != 0))
    return total_sum