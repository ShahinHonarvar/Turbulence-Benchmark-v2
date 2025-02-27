def sum_in_range(numbers):
    total = 0
    for number in numbers:
        if 4 <= number <= 5:
            total += number
    return total