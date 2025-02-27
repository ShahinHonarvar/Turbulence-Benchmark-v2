def sum_in_range(numbers):
    total = sum((number for number in numbers if -97 <= number <= -48))
    return total