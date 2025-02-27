def sum_in_range(numbers):
    total = 0
    for number in numbers:
        if 18 <= number <= 60:
            total += number
    return total