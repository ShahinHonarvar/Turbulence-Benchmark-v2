def sum_in_range(numbers):
    total = 0
    for number in numbers:
        if 6 <= number <= 9:
            total += number
    return total