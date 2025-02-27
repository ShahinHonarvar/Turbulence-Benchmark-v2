def sum_in_range(numbers):
    total = 0
    for number in numbers:
        if 15 <= number <= 57:
            total += number
    return total